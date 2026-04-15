import requests
import boto3
from datetime import datetime,timezone
import logging
class Solution:
    logging.basicConfig(level=logging.INFO)
    logger=logging.getLogger(__name__)
    S3_bucket='s3_bronze_data'
    API_request='https://'
    current_date=datetime.now(timezone.utc)
    def fetch_data():
        
        
        try:
           response=requests.get(API_URL,timeout=10)
           response.raise_for_status()
           return response.json()
        except requests.RequestException as e:
            logger.error(f"API request failed with {e}")
            raise
    
    def upload_date(data):
        
        current_year=current_date.year
        current_month=current_date.month
        current_day=current_date.date
        current_hour=current_date.hour

        key='messages/'+current_year+'/'+current_month+'/'+current_day+'/'+current_hour+'/'+'message_'+current_date+'.json'
        s3=boto3.client("s3")

        try:
            s3.put_object(Bucket=S3_bucket,Key=key,Body=str(data))
            logger.info(f"file is uploaded with key={key}")
        except Exception as e:
            logger.error(f"S3 upload failed with {e}")
            raise
    
    def main ():
        logger.info(f"Start bronze layer ingestion at {current_date} ")
        data=fetch_data()
        upload_data(data)
        logger.info(f"End of module {__name__} at {current_date} " )
    if __name__=="__main__":
        main()


            
        


        

        