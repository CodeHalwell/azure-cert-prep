"""
Multi-modal AI assistant using GPT-4o.
"""

import base64
import json
from openai import AzureOpenAI
from tools import TOOLS, execute_tool
import os


class MultiModalAssistant:
    """Multi-modal assistant with vision, audio, and tool capabilities."""

    def __init__(self):
        self.client = AzureOpenAI(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_KEY"),
            api_version="2024-02-15-preview",
        )
        self.model = "gpt-4o"
        self.conversation_history = []
        
        self.system_prompt = """You are a helpful multi-modal AI assistant.
You can:
- Understand and describe images
- Answer questions about visual content
- Execute tools when asked
- Maintain conversation context

Be helpful, accurate, and concise."""

    def chat(
        self,
        message: str,
        image_url: str = None,
        image_base64: str = None,
    ) -> str:
        """
        Send a message with optional image.

        Args:
            message: User's text message
            image_url: URL of image to analyze
            image_base64: Base64-encoded image

        Returns:
            Assistant's response
        """
        # Build message content
        content = []
        content.append({"type": "text", "text": message})

        if image_url:
            content.append({
                "type": "image_url",
                "image_url": {"url": image_url},
            })
        elif image_base64:
            content.append({
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"},
            })

        # Add to history
        self.conversation_history.append({
            "role": "user",
            "content": content if len(content) > 1 else message,
        })

        # Build messages
        messages = [
            {"role": "system", "content": self.system_prompt},
            *self.conversation_history,
        ]

        # Call API
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
            max_tokens=1000,
        )

        assistant_message = response.choices[0].message

        # Handle tool calls
        if assistant_message.tool_calls:
            tool_results = []
            for tool_call in assistant_message.tool_calls:
                result = execute_tool(
                    tool_call.function.name,
                    json.loads(tool_call.function.arguments),
                )
                tool_results.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result,
                })

            # Add tool results and get final response
            self.conversation_history.append(assistant_message)
            self.conversation_history.extend(tool_results)

            follow_up = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    *self.conversation_history,
                ],
            )
            final_response = follow_up.choices[0].message.content
            self.conversation_history.append({
                "role": "assistant",
                "content": final_response,
            })
            return final_response

        # No tool calls
        self.conversation_history.append({
            "role": "assistant",
            "content": assistant_message.content,
        })
        return assistant_message.content

    def analyze_image(self, image_path: str, question: str = "Describe this image") -> str:
        """Analyze a local image file."""
        with open(image_path, "rb") as f:
            image_data = base64.b64encode(f.read()).decode("utf-8")
        return self.chat(question, image_base64=image_data)

    def clear_history(self):
        """Clear conversation history."""
        self.conversation_history = []


if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()

    assistant = MultiModalAssistant()

    print("Multi-modal Assistant - type 'exit' to quit")
    print("Prefix with 'image:' to analyze an image URL\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        if user_input.startswith("image:"):
            parts = user_input[6:].split(" ", 1)
            image_url = parts[0]
            question = parts[1] if len(parts) > 1 else "Describe this image"
            response = assistant.chat(question, image_url=image_url)
        else:
            response = assistant.chat(user_input)

        print(f"Assistant: {response}\n")
