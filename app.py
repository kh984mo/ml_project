import sys
sys.path.append('./src')

# from mlprojects import logger
# from src.mlproject.logger import logging
from mlproject.logger import logging
from mlproject.exception import CustomException
from mlproject.components.data_ingestion import DataIngestion
from mlproject.components.data_ingestion import DataIngestionConfig
if __name__=="__main__":
    logging.info("the execution has started")

    try:
        # data_ingestion=DataIngestionConfig()
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("custom exception")
        raise CustomException(e,sys)
