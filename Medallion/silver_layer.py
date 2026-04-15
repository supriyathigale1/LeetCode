import pandas as pd
from datetime import datetime,timezone,timedelta
import logging
from io import BytesIO

logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)
current_date=datetime.now(timezone=utc)
silver_prefix='message-silver/'
bronze_prefix='message-bronze/'
bucket='socialmedia'
def clean_data(df: pd.DataFrame)->pd.DataFrame:
    try :
        df=df.copy()
        df["order_date"]=pd.to_datetime(df["order_datetime"])
        df["total"]=pd.to_numeric(df["quantity"]*df["price"])
        df=df.dropna(subset="order_id")
        df=df.drop_duplicates(subset="order_id")
        logger.info(f"Data has been cleaned at {current_date}")
    except Exception as e:
        logger.error(f"Data cleaning has  failed at {current_date} with {e}")
        raise Exception
    return df

def upload_silver_data(s3bronzedata):
    try:
        buffer=BytesIO()
        s3bronzedata.to_parquet(buffer,index=False)

        key=silver_prefix+current_date.year+'/'+current_date.month+'/'+current_day+'/'+current_hour+'/'+silverfile+current_date+'.parquet'

        s3.put_object(Bucket=bucket,Key=key,Body=buffer.getvalue())
        logger.error(f"Upload of silver data suceeded at {bucket}+ {key}")
    except Exception as e:
        logger.error(f"Upload of silver data failed with {e}")
        raise error

def get_2_days_keys():
    today=current_date.date()
    yesterday=today-timedelta(days=1) 

    keys=[ bronze_prefix+current_date.year+'/'+current_date.month+'/'+current_day+'/'+current_hour+'/'+current_date+'.json',
    bronze_prefix+yesterday.year+'/'+yesterday.month+'/'+yesterday.day+'/'+yesterday.hour+'/'+yesterday.datetime+'.json'


    ]
    return keys

def read_bronze_layer(keys):
    dfs=[]
    try:
        logger.info(f"Reading bronze data ")
        for key1 in keys:
            obj=s3.get_object(Bucket=bucket,Key=key1)
            data=obj['Body']
            df=pd.read_json(data)
            dfs.append(df)
        if dfs:
            return pd.concat(dfs, ignore_index=True)
        else:
            pd.DataFrame()
    except Exception as e:
        logger.error(f"Read failedwith {e}")
        raise error

def main():
    logger.info(f"Start silver job ingestion at {current_date}")
    keys=get_2_days_keys()
    df=read_bronze_layer(keys)
    if not df:
        logger.info(f"No data found at {current_date}")
        return
    df_clean=clean_data(df)
    upload_silver_data(df_clean)
    logger.info(f"silver job ingestion completed at {current_date}")
if __name__ ="__main__":
    main()




