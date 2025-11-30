"""
Anomaly detection service using Azure Anomaly Detector.
"""

import os
from datetime import datetime, timedelta
from azure.ai.anomalydetector import AnomalyDetectorClient
from azure.ai.anomalydetector.models import (
    UnivariateDetectionOptions,
    TimeSeriesPoint,
    TimeGranularity,
)
from azure.core.credentials import AzureKeyCredential


class AnomalyDetectorService:
    """Azure Anomaly Detector client."""

    def __init__(self):
        self.client = AnomalyDetectorClient(
            endpoint=os.getenv("AZURE_ANOMALY_DETECTOR_ENDPOINT"),
            credential=AzureKeyCredential(os.getenv("AZURE_ANOMALY_DETECTOR_KEY")),
        )

    def detect_batch(
        self,
        series: list[dict],
        granularity: str = "minutely",
        sensitivity: int = 95,
    ) -> list[dict]:
        """
        Detect anomalies in a batch of time series data.

        Args:
            series: List of {"timestamp": datetime, "value": float}
            granularity: Time granularity (minutely, hourly, daily)
            sensitivity: Detection sensitivity (0-100)

        Returns:
            List of detected anomalies
        """
        points = [
            TimeSeriesPoint(timestamp=p["timestamp"], value=p["value"])
            for p in series
        ]

        granularity_map = {
            "minutely": TimeGranularity.MINUTELY,
            "hourly": TimeGranularity.HOURLY,
            "daily": TimeGranularity.DAILY,
        }

        options = UnivariateDetectionOptions(
            series=points,
            granularity=granularity_map.get(granularity, TimeGranularity.MINUTELY),
            custom_interval=None,
            sensitivity=sensitivity,
        )

        result = self.client.detect_univariate_entire_series(options)

        anomalies = []
        for i, is_anomaly in enumerate(result.is_anomaly):
            if is_anomaly:
                anomalies.append({
                    "timestamp": series[i]["timestamp"],
                    "value": series[i]["value"],
                    "expected_value": result.expected_values[i],
                    "upper_margin": result.upper_margins[i],
                    "lower_margin": result.lower_margins[i],
                    "is_negative_anomaly": result.is_negative_anomaly[i],
                    "is_positive_anomaly": result.is_positive_anomaly[i],
                })

        return anomalies

    def detect_last_point(
        self,
        series: list[dict],
        granularity: str = "minutely",
        sensitivity: int = 95,
    ) -> dict:
        """
        Detect if the last point in the series is an anomaly.

        Args:
            series: List of {"timestamp": datetime, "value": float}
            granularity: Time granularity
            sensitivity: Detection sensitivity

        Returns:
            Detection result for last point
        """
        points = [
            TimeSeriesPoint(timestamp=p["timestamp"], value=p["value"])
            for p in series
        ]

        granularity_map = {
            "minutely": TimeGranularity.MINUTELY,
            "hourly": TimeGranularity.HOURLY,
            "daily": TimeGranularity.DAILY,
        }

        options = UnivariateDetectionOptions(
            series=points,
            granularity=granularity_map.get(granularity, TimeGranularity.MINUTELY),
            sensitivity=sensitivity,
        )

        result = self.client.detect_univariate_last_point(options)

        return {
            "is_anomaly": result.is_anomaly,
            "expected_value": result.expected_value,
            "upper_margin": result.upper_margin,
            "lower_margin": result.lower_margin,
            "is_negative_anomaly": result.is_negative_anomaly,
            "is_positive_anomaly": result.is_positive_anomaly,
            # Severity is only available in certain API versions
            "severity": getattr(result, "severity", None),
        }


if __name__ == "__main__":
    from dotenv import load_dotenv
    import random

    load_dotenv()

    # Generate sample data with an anomaly
    now = datetime.utcnow()
    series = []
    for i in range(100):
        timestamp = now - timedelta(minutes=100 - i)
        value = 50 + random.gauss(0, 5)
        # Inject anomaly at position 80
        if i == 80:
            value = 100
        series.append({"timestamp": timestamp, "value": value})

    detector = AnomalyDetectorService()

    print("Running batch detection...")
    anomalies = detector.detect_batch(series)
    print(f"Found {len(anomalies)} anomalies:")
    for a in anomalies:
        print(f"  - {a['timestamp']}: value={a['value']}, expected={a['expected_value']:.2f}")

    print("\nChecking last point...")
    last_result = detector.detect_last_point(series)
    print(f"Is anomaly: {last_result['is_anomaly']}")
