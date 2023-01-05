import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pydataset import data
from scipy import stats

from env import host, username, password    # import needed for get_connection() to operate





# Function to build the connection between notebook and MySql. Will be used in other functions.
# Returns the string that is neccessary for that connection.
def get_connection(db, user = username, host = host, password = password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'





# Acquire telco dataset from SQL database
def get_telco_data():
    filename = "telco.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col=0)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql('''
                            SELECT * 
                            FROM customers
                            JOIN contract_types as ct USING(contract_type_id)
                            JOIN internet_service_types as ist USING(internet_service_type_id)
                            JOIN payment_types as pt USING(payment_type_id)
                    ''', get_connection('telco_churn'))

        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename, index=False)

        # Return the dataframe to the calling code
        return df  



# url = get_db_url('db')
# pd.read_sql('Query', url)