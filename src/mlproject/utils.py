import sys
import os
sys.path.append('./src')
from mlproject.logger import logging
from mlproject.exception import CustomException
import pandas as pd
from dotenv import load_dotenv
import pymysql
load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")

def read_sql_data():
    logging.info("Reading data  from Sql Dtabases")

    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("connection establish",mydb)
        df=pd.read_sql_query('select * from students',mydb)
        print(df.head())
        return df
    except Exception as ex:
        raise CustomException(ex,sys)

