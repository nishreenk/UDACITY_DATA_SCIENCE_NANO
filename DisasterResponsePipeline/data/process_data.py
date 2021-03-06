# Import Python and required libraries 
import sys
import pandas as pd
import numpy as np
import re
import sqlalchemy
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    ''' Load messages.csv into a dataframe and inspect the first few lines.
        Load categories.csv into a dataframe and inspect the first few lines.
    '''
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = messages.merge(categories, on='id')
    return df

def clean_data(df):
    '''Clean the data, separate categories columns, remove duplicates, 
        modify the dataframe to add the 36 individual category columns,
        drop responses labeled as'2'. They are only 188 of them.'''
    
    categories_df = df['categories'].str.split(';', expand=True)
    #categories =  categories.categories.str.split(';', expand=True)
    # select the first row of the categories dataframe
    row = categories_df.loc[0]
    category_colnames =[]
    for x in range(row.shape[0]):
        category_colnames.append(row[x][:-2])
    # rename the columns of `categories`
    categories_df.columns = category_colnames
   
    
    for column in categories_df:
        # set each value to be the last character of the string
        #categories[column] = categories[column].apply(lambda x: re.sub(column, "", x))
        categories_df[column] = categories_df[column].apply(lambda x: re.sub("[^0-9]", "", x))

        # convert column from string to numeric
        categories_df[column] = np.abs(pd.to_numeric(categories_df[column]))
    
    # drop the original categories column from `df`
    df.drop(columns='categories', inplace=True)
    
    # concatenate the original dataframe with the new `categories` dataframe
    df = pd.concat([df, categories_df], axis=1)
    
    # check number of duplicates
    # Select duplicate rows except first occurrence based on all columns
    duplicateRowsDF = df[df.duplicated()]
    
    # drop duplicates
    df.drop_duplicates(keep="first", inplace=True)
    
    #drop 188 rows with 'related' category response '2'  : 2=not disaster related , which means 1=disaster related, zero presumably = missing
    df = df[df['related'] != 2]
    
    return df
    
    
def save_data(df, database_filename):
    '''Save the dataframe in a sqlite database'''
    
    engine = create_engine('sqlite:///{}'.format(database_filename))
    df.to_sql(database_filename, engine, index=False, if_exists='replace') 


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
