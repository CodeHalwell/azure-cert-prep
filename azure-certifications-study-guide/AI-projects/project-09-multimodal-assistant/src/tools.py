"""
Tool definitions and execution for the assistant.
"""

from datetime import datetime
import requests

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "City name"},
                },
                "required": ["city"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_time",
            "description": "Get current time",
            "parameters": {"type": "object", "properties": {}},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_web",
            "description": "Search the web for information",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query"},
                },
                "required": ["query"],
            },
        },
    },
]


def get_weather(city: str) -> str:
    """Simulated weather lookup."""
    return f"Weather in {city}: Sunny, 22°C (simulated)"


def get_time() -> str:
    """Get current time."""
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")


def search_web(query: str) -> str:
    """Simulated web search."""
    return f"Search results for '{query}': [Simulated results would appear here]"


def execute_tool(name: str, arguments: dict) -> str:
    """Execute a tool by name."""
    tools = {
        "get_weather": lambda args: get_weather(args["city"]),
        "get_time": lambda args: get_time(),
        "search_web": lambda args: search_web(args["query"]),
    }
    
    if name in tools:
        return tools[name](arguments)
    return f"Unknown tool: {name}"
