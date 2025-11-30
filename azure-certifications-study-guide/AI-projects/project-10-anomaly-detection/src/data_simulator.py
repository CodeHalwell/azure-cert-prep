"""
Data simulator for anomaly detection testing.
"""

import json
import random
import time
from datetime import datetime
from azure.eventhub import EventHubProducerClient, EventData
import os


class DataSimulator:
    """Simulates time series data with occasional anomalies."""

    def __init__(self, connection_string: str, event_hub_name: str):
        self.producer = EventHubProducerClient.from_connection_string(
            conn_str=connection_string,
            eventhub_name=event_hub_name,
        )
        self.base_value = 50
        self.anomaly_probability = 0.02  # 2% chance of anomaly

    def generate_point(self) -> dict:
        """Generate a single data point."""
        timestamp = datetime.utcnow()
        
        # Normal value with Gaussian noise
        value = self.base_value + random.gauss(0, 5)
        
        # Occasionally inject an anomaly
        is_anomaly = random.random() < self.anomaly_probability
        if is_anomaly:
            # Anomaly: spike or drop
            if random.random() > 0.5:
                value = self.base_value + random.uniform(30, 50)  # Spike
            else:
                value = self.base_value - random.uniform(30, 40)  # Drop

        return {
            "timestamp": timestamp.isoformat(),
            "value": round(value, 2),
            "device_id": "sensor_001",
            "is_injected_anomaly": is_anomaly,
        }

    def send_event(self, data: dict) -> None:
        """Send data to Event Hub."""
        event_data_batch = self.producer.create_batch()
        event_data_batch.add(EventData(json.dumps(data)))
        self.producer.send_batch(event_data_batch)

    def run(self, interval_seconds: int = 1, duration_minutes: int = 60):
        """Run continuous data simulation."""
        print(f"Starting data simulation for {duration_minutes} minutes...")
        
        end_time = time.time() + (duration_minutes * 60)
        count = 0
        anomaly_count = 0

        try:
            while time.time() < end_time:
                point = self.generate_point()
                self.send_event(point)
                count += 1
                
                if point["is_injected_anomaly"]:
                    anomaly_count += 1
                    print(f"⚠️  Anomaly injected: {point['value']}")
                else:
                    print(f"📊 Sent: {point['value']}")
                
                time.sleep(interval_seconds)
        except KeyboardInterrupt:
            print("\nSimulation stopped by user")
        finally:
            self.producer.close()
            print(f"\nTotal points: {count}, Anomalies injected: {anomaly_count}")


if __name__ == "__main__":
    from dotenv import load_dotenv
    import argparse

    load_dotenv()

    parser = argparse.ArgumentParser()
    parser.add_argument("--interval", type=int, default=1, help="Seconds between points")
    parser.add_argument("--duration", type=int, default=10, help="Duration in minutes")
    args = parser.parse_args()

    connection_string = os.getenv("EVENT_HUB_CONNECTION_STRING")
    event_hub_name = os.getenv("EVENT_HUB_NAME", "telemetry")

    if not connection_string:
        print("Set EVENT_HUB_CONNECTION_STRING environment variable")
        exit(1)

    simulator = DataSimulator(connection_string, event_hub_name)
    simulator.run(interval_seconds=args.interval, duration_minutes=args.duration)
