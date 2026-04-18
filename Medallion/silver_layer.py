import pandas as pd
import boto3
from datetime import datetime, timezone, timedelta
import logging
from io import BytesIO

# Silver Layer - Medallion Architecture
# The silver layer is the cleaned and transformed data layer.
# It takes raw data from bronze layer, applies data quality rules,
# and stores cleaned, validated data ready for analytics.

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration constants
current_date = datetime.now(timezone.utc)
silver_prefix = 'message-silver/'
bronze_prefix = 'message-bronze/'
bucket = 'socialmedia'

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform bronze layer data for silver layer.

    Args:
        df: Raw DataFrame from bronze layer

    Returns:
        Cleaned and transformed DataFrame

    Raises:
        Exception: If data cleaning fails
    """
    try:
        df = df.copy()
        # Convert datetime column
        df["order_date"] = pd.to_datetime(df["order_datetime"])
        # Calculate total price
        df["total"] = pd.to_numeric(df["quantity"] * df["price"])
        # Remove rows with missing order_id
        df = df.dropna(subset=["order_id"])
        # Remove duplicate orders
        df = df.drop_duplicates(subset=["order_id"])
        logger.info(f"Data cleaning completed at {current_date}")
        return df
    except Exception as e:
        logger.error(f"Data cleaning failed at {current_date} with {e}")
        raise Exception(f"Data cleaning failed: {e}")

def upload_silver_data(df_clean):
    """
    Upload cleaned data to silver layer S3 bucket in Parquet format.

    Args:
        df_clean: Cleaned DataFrame to upload

    Raises:
        Exception: If upload fails
    """
    try:
        # Convert DataFrame to Parquet format in memory
        buffer = BytesIO()
        df_clean.to_parquet(buffer, index=False)

        # Create partitioned S3 key
        current_day = current_date.day
        current_hour = current_date.hour
        silver_file = 'silver_data'
        key = f"{silver_prefix}{current_date.year}/{current_date.month}/{current_day}/{current_hour}/{silver_file}_{current_date}.parquet"

        # Upload to S3
        s3 = boto3.client("s3")
        s3.put_object(Bucket=bucket, Key=key, Body=buffer.getvalue())
        logger.info(f"Silver data upload succeeded to {bucket}/{key}")
    except Exception as e:
        logger.error(f"Silver data upload failed with {e}")
        raise Exception(f"Upload failed: {e}")

def get_2_days_keys():
    """
    Generate S3 keys for bronze layer data from today and yesterday.

    Returns:
        List of S3 keys for the last 2 days
    """
    today = current_date.date()
    yesterday = today - timedelta(days=1)

    keys = [
        f"{bronze_prefix}{current_date.year}/{current_date.month}/{current_date.day}/{current_date.hour}/{current_date}.json",
        f"{bronze_prefix}{yesterday.year}/{yesterday.month}/{yesterday.day}/{yesterday.hour}/{yesterday}.json"
    ]
    return keys

def read_bronze_layer(keys):
    """
    Read bronze layer data from S3 for the given keys.

    Args:
        keys: List of S3 keys to read

    Returns:
        Combined DataFrame from all keys, or empty DataFrame if no data

    Raises:
        Exception: If reading fails
    """
    dfs = []
    try:
        logger.info("Reading bronze layer data")
        s3 = boto3.client("s3")

        for key in keys:
            try:
                obj = s3.get_object(Bucket=bucket, Key=key)
                data = obj['Body']
                df = pd.read_json(data)
                dfs.append(df)
            except s3.exceptions.NoSuchKey:
                logger.warning(f"Key not found: {key}")
                continue

        if dfs:
            return pd.concat(dfs, ignore_index=True)
        else:
            return pd.DataFrame()
    except Exception as e:
        logger.error(f"Bronze layer read failed with {e}")
        raise Exception(f"Read failed: {e}")

def main():
    """
    Main execution function for the silver layer pipeline.
    """
    logger.info(f"Starting silver layer ingestion at {current_date}")
    keys = get_2_days_keys()
    df = read_bronze_layer(keys)

    if df.empty:
        logger.info(f"No data found at {current_date}")
        return

    df_clean = clean_data(df)
    upload_silver_data(df_clean)
    logger.info(f"Silver layer ingestion completed at {datetime.now(timezone.utc)}")

# Execute the silver layer pipeline when script is run directly
if __name__ == "__main__":
    main()




