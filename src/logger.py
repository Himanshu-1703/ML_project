import logging
import os
from datetime import datetime as dt


log_file  = f"{dt.now().strftime('%d_%m_%Y_%H_%M_%S')}"
logs_path = os.path.join(os.getcwd(),'logs',log_file)

os.makedirs(name=logs_path,exist_ok=True)

log_file_path = os.path.join(logs_path,log_file,'.log')


logging.basicConfig(
    filename=log_file_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

