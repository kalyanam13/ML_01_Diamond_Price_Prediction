import os
import sys
import logging
#from src.logger import logging
import src.exception.CustomException 
import pandas as pd

from src.components.data_ingestion import DataIngestion

if __name__=='__main__':
    obj=DataIngestion()
    train_data_path,test_data_path = obj.initiate_data_ingestion()
    print(train_data_path,test_data_path)