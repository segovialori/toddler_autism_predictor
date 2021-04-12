import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

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
    dummies = pd.get_dummies(df[['sex']], drop_first=True)
    df = pd.concat([df, dummies], axis=1) 
    binary(df)
    df['asd_traits'] = df[['asd_traits']].replace({'No': 0, 'Yes': 1})
    df['ethnicity'] = df[['ethnicity']].replace({'White European': 1,
                                             'asian': 2, 
                                             'middle eastern': 3, 
                                             'south asian': 2, 
                                             'black': 4, 
                                             'Hispanic': 5, 
                                             'Others': 6, 
                                             'Latino': 5, 
                                             'mixed': 6,
                                             'Pacifica': 6,
                                             'Native Indian': 6})
    df.drop(columns = ['Qchat-10-Score', 'Who completed the test', 'sex'], inplace=True)
    df = df.set_index('Case_No')
    return df
                


#function to change columns from yes/no to o/1
def binary(df):
    binary_columns = ['jaundice','family_mem_with_asd']
    for feature in binary_columns:
        df[feature].replace(to_replace='yes', value=1, inplace=True)
        df[feature].replace(to_replace='no', value=0, inplace=True)


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

    #SCALE
def Standard_Scaler(X_train, X_validate, X_test):
    """
    Takes in X_train, X_validate and X_test dfs with numeric values only
    Returns scaler, X_train_scaled, X_validate_scaled, X_test_scaled dfs
    """

    scaler = StandardScaler().fit(X_train)
    X_train_scaled = pd.DataFrame(scaler.transform(X_train), index = X_train.index, columns = X_train.columns)
    X_validate_scaled = pd.DataFrame(scaler.transform(X_validate), index = X_validate.index, columns = X_validate.columns)
    X_test_scaled = pd.DataFrame(scaler.transform(X_test), index = X_test.index, columns = X_test.columns)
    
    return scaler, X_train_scaled, X_validate_scaled, X_test_scaled

def chi2(df, var, target, alpha):
    '''
    This function takes in a df, variable, a target variable, and the alpha, and runs a chi squared test. Statistical analysis is printed in the output.
    '''
    observed = pd.crosstab(df[var], df[target])
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    print('Observed\n')
    print(observed.values)
    print('---\nExpected\n')
    print(expected)
    print('---\n')
    print(f'chi^2 = {chi2:.4f}')
    print(f'p     = {p:.4f}\n')
    if p < alpha:
        print(f'Becasue the p-value: {round(p, 4)} is less than alpha: {alpha}, we can reject the null hypothesis')
    else:
        print('There is insufficient evidence to reject the null hypothesis')