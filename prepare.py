import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split  # import needed for the train, test, split functions.





# Function for cleaning Telco data
def prep_telco(telco):
    ''' 
        This functions cleans the data by dropping dupes, dropping unnecesssary columns,
         simplifying column names, creating dummy columns, renaming them, and concatenating 
         the dummy df to the main df. Also, created a new column 'churn numeric'. Reset index
         so that first column does not become the index.
    '''
    telco = telco.reset_index()
    telco = telco.drop_duplicates()
    telco = telco.drop(['payment_type_id','internet_service_type_id', 'contract_type_id'], axis=1)
    telco_dummies = pd.get_dummies(telco[['dependents','multiple_lines','online_security','contract_type']], dummy_na=False, drop_first=False)
    telco = pd.concat([telco, telco_dummies], axis=1)
    telco = telco.rename(columns={'online_security_No_internet_service': 'online_security_no_internet',\
                                    'online_security_Yes': 'online_security_yes_internet',\
                                    'multiple_lines_No_phone_service':'multiple_lines_no',\
                                    'multiple_lines_Yes': 'multiple_lines_yes'})
    telco.columns = [x.lower() for x in telco.columns]
    telco['churn_numeric'] = telco.churn.str.replace('No','0').str.replace('Yes','1').astype(int)
    return telco





# Function for Training, Validating, and Testing the data. 
def split_data(df, target= 'enter target column here'):
    ''' 
        This function is the train, validate, test, function.
        1. First we create the TRAIN and TEST dataframes at an 0.80 train_size( or test_size 0.2).

        2. Second, use the newly created TRAIN dataframe and split that at a 0.70 train_size
        ( or test_size 0.3), which means 70% of the train dataframe, so 56% of all the data.

        Now we have a train, validate, and test dataframes

    '''
    train, test = train_test_split(df, train_size=0.8, random_state=123, stratify=df[target])
    train, validate = train_test_split(train, train_size = 0.7, random_state = 123, stratify=train[target])
    return train, validate, test