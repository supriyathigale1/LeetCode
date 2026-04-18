import requests
import boto3
from datetime import datetime, timezone
import logging

# Bronze Layer - Medallion Architecture
# The bronze layer is the raw data ingestion layer that collects data from various sources
# and stores it in its original format without transformation.

class BronzeLayer:
    """
    Bronze layer implementation for data ingestion in medallion architecture.
    Handles API data fetching and S3 storage of raw data.
    """

    # Configure logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Configuration constants
    S3_BUCKET = 's3_bronze_data'  # S3 bucket for storing raw data
    API_URL = 'https://'  # API endpoint URL (placeholder)
    current_date = datetime.now(timezone.utc)  # Current timestamp in UTC

    @staticmethod
    def fetch_data():
        """
        Fetch data from the configured API endpoint.

        Returns:
            JSON data from the API response

        Raises:
            requests.RequestException: If the API request fails
        """
        try:
            response = requests.get(BronzeLayer.API_URL, timeout=10)
            response.raise_for_status()  # Raise exception for bad status codes
            return response.json()
        except requests.RequestException as e:
            BronzeLayer.logger.error(f"API request failed with {e}")
            raise

    @staticmethod
    def upload_data(data):
        """
        Upload data to S3 with partitioned key structure.

        Args:
            data: The data to upload (will be converted to string)

        Raises:
            Exception: If S3 upload fails
        """
        # Extract date components for partitioning
        current_year = BronzeLayer.current_date.year
        current_month = BronzeLayer.current_date.month
        current_day = BronzeLayer.current_date.day  # Fixed: was .date which is wrong
        current_hour = BronzeLayer.current_date.hour

        # Create partitioned S3 key: messages/year/month/day/hour/message_timestamp.json
        key = f'messages/{current_year}/{current_month}/{current_day}/{current_hour}/message_{BronzeLayer.current_date}.json'

        # Initialize S3 client
        s3 = boto3.client("s3")

        try:
            s3.put_object(Bucket=BronzeLayer.S3_BUCKET, Key=key, Body=str(data))
            BronzeLayer.logger.info(f"File uploaded successfully with key={key}")
        except Exception as e:
            BronzeLayer.logger.error(f"S3 upload failed with {e}")
            raise

    @staticmethod
    def main():
        """
        Main execution function for the bronze layer pipeline.
        """
        BronzeLayer.logger.info(f"Starting bronze layer ingestion at {BronzeLayer.current_date}")
        data = BronzeLayer.fetch_data()
        BronzeLayer.upload_data(data)
        BronzeLayer.logger.info(f"Completed bronze layer processing at {datetime.now(timezone.utc)}")

# Execute the bronze layer pipeline when script is run directly
if __name__ == "__main__":
    BronzeLayer.main()


            
        


        

        