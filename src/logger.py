#import logging 
#import os
#from datetime import datetime

#LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
#os.makedirs(logs_path,exist_ok=True)

#LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

#logging.basicConfig(
    #filename=LOG_FILE_PATH,
    #format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    #level=logging.INFO
#)

import logging

def setup_logging(log_file='app.log'):
    """Configure logging to write to both console and file."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

# Call setup_logging when this module is imported
setup_logging()