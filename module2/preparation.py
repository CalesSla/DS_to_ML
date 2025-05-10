from collection import load_data_from_db
import pandas as pd
import re
from loguru import logger
import warnings
warnings.filterwarnings("ignore")

def prepare_data():
    logger.info("starting up preprocessing pipeline")
    data = load_data_from_db()
    data_encoded = encode_cat_cols(data)
    df = parse_garden_col(data_encoded)
    return df

def encode_cat_cols(data):
    cols = ["balcony", "parking", "furnished", "garage", "storage"]
    logger.info(f"encoding categorical columns {cols}")
    data_encoded = pd.get_dummies(data, 
                                  columns = cols, 
                                  drop_first=True, 
                                  dtype=int)

    return data_encoded

def parse_garden_col(data):
    logger.info("parsing garden column")
    for i in range(len(data)):
        if data.garden[i] == 'Not present':
            data.garden[i] = 0
        else:
            data.garden[i] = int(re.findall(r"\d+", data.garden[i])[0])
    return data