from collection import load_data
import pandas as pd
import re
import warnings
warnings.filterwarnings("ignore")

def prepare_data():
    data = load_data()
    data_encoded = encode_cat_cols(data)
    df = parse_garden_col(data_encoded)
    return df

def encode_cat_cols(data):
    data_encoded = pd.get_dummies(data, 
                                  columns = ["balcony", 
                                             "parking", 
                                             "furnished", 
                                             "garage", 
                                             "storage"], 
                                  drop_first=True, 
                                  dtype=int)

    return data_encoded

def parse_garden_col(data):
    for i in range(len(data)):
        if data.garden[i] == 'Not present':
            data.garden[i] = 0
        else:
            data.garden[i] = int(re.findall(f"\d+", data.garden[i])[0])

    return data