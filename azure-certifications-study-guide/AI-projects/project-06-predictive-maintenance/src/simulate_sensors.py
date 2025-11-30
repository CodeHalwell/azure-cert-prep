"""
Simulated IoT sensor data generator for predictive maintenance.
"""

import json
import random
import time
from datetime import datetime
from azure.iot.device import IoTHubDeviceClient, Message


class SensorSimulator:
    """Simulates IoT sensor data for equipment monitoring."""

    def __init__(self, connection_string: str, device_id: str):
        self.client = IoTHubDeviceClient.create_from_connection_string(connection_string)
        self.device_id = device_id
        self.operational_hours = random.randint(500, 5000)
        
        # Base values
        self.base_temperature = 65.0
        self.base_vibration = 0.3
        self.base_pressure = 100.0
        
        # Degradation rate (simulates wear)
        self.degradation = 0.0

    def generate_reading(self) -> dict:
        """Generate a single sensor reading."""
        # Add random variation and degradation effect
        temperature = self.base_temperature + random.gauss(0, 2) + (self.degradation * 5)
        vibration = self.base_vibration + random.gauss(0, 0.05) + (self.degradation * 0.1)
        pressure = self.base_pressure + random.gauss(0, 1) - (self.degradation * 2)
        
        # Simulate gradual degradation
        self.degradation += random.uniform(0, 0.001)
        self.operational_hours += 1 / 60  # 1 minute per reading
        
        return {
            "device_id": self.device_id,
            "timestamp": datetime.utcnow().isoformat(),
            "temperature": round(temperature, 2),
            "vibration": round(vibration, 4),
            "pressure": round(pressure, 2),
            "operational_hours": round(self.operational_hours, 1),
        }

    def send_telemetry(self, reading: dict) -> None:
        """Send telemetry to IoT Hub."""
        message = Message(json.dumps(reading))
        message.content_encoding = "utf-8"
        message.content_type = "application/json"
        
        self.client.send_message(message)
        print(f"Sent: {reading}")

    def run(self, interval_seconds: int = 60):
        """Run continuous sensor simulation."""
        print(f"Starting sensor simulation for {self.device_id}")
        
        try:
            while True:
                reading = self.generate_reading()
                self.send_telemetry(reading)
                time.sleep(interval_seconds)
        except KeyboardInterrupt:
            print("Simulation stopped")
        finally:
            self.client.shutdown()


if __name__ == "__main__":
    import os
    
    connection_string = os.getenv("IOT_DEVICE_CONNECTION_STRING")
    device_id = os.getenv("DEVICE_ID", "sensor001")
    
    if not connection_string:
        print("Set IOT_DEVICE_CONNECTION_STRING environment variable")
        exit(1)
    
    simulator = SensorSimulator(connection_string, device_id)
    simulator.run(interval_seconds=10)
