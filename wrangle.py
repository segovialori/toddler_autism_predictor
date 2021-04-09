import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.model_selection import train_test_split

def wrangle_autism():
    '''
    This function will acquire data locally and turn dataset into
    a clean dataframe
    '''
    df = pd.read_csv('Toddler Autism dataset July 2018.csv')
    df.rename(columns={'A1': 'name_response', 
                       'A2': 'eye_contact', 
                       'A3': 'pointing', 
                       'A4': 'shared_interest', 
                       'A5': 'pretend_play', 
                       'A6': 'joint_attention', 
                       'A7': 'emotions',
                       'A8': 'vocal',
                       'A9': 'gestures',
                       'A10': 'blank_gaze',
                       'Age_Mons': 'age',
                       'Sex': 'sex',
                       'Ethnicity': 'ethnicity',
                       'Jaundice': 'jaundice',
                       'Family_mem_with_ASD': 'family_mem_with_asd',
                       'Class/ASD Traits ': 'asd_traits'}, inplace=True)
    df.drop(columns = ['Qchat-10-Score', 'Who completed the test'], inplace=True)
    df = df.set_index('Case_No')
    return df

#split with 
def train_validate_test_split(df, target, seed):
    '''
    spilts our data  into train, validate, test
    by taking in a dataframe and dividing into
    separate
    '''
    # Train, Validate, and test
    train_and_validate, test = train_test_split(
        df, test_size=0.2, random_state=seed)
    train, validate = train_test_split(
        train_and_validate,
        test_size=0.3,
        random_state=seed)
    
    # Split with X and y
    X_train = train.drop(columns=[target])
    y_train = train[target]
    
    X_validate = validate.drop(columns=[target])
    y_validate = validate[target]
    
    X_test = test.drop(columns=[target])
    y_test = test[target]
    
    return train, validate, test, X_train, y_train, X_validate, y_validate, X_test, y_test   