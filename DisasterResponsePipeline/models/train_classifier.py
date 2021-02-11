import sys
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import re
import nltk
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
from nltk.tokenize import TweetTokenizer 
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report, recall_score, confusion_matrix
import requests
import sqlalchemy
from sqlalchemy import create_engine
import pickle


def load_data(database_filepath):
    #engine = create_engine('sqlite:///' + database_filepath)
    engine = create_engine('sqlite:///data/DisasterResponse.db')
    #engine = create_engine('sqlite:///%s' % database_filepath)
    #engine = create_engine('sqlite:///' + database_filepath)
    #engine = create_engine('sqlite:///{}'.format(database_filepath))
    print(engine.table_names())
    df = pd.read_sql_table('data/DisasterResponse.db', con=engine)
    X =  df['message'].values  
    Y = df.iloc[:, 5:].values
    Y = Y.astype(int)
    category_names = list(df.columns[5:])
    return X,Y, category_names

def tokenize(text):
    '''
    Function to tokenize the text messages
    Input: text
    output: cleaned tokenized text as a list object
    '''
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    tweet_tokenizer = TweetTokenizer()
    # remove numbers
    s = re.sub(r'[\d-]+ ', '', text)
    
    ## Tokenize and remove stop words
    tokens = [word for word in tweet_tokenizer.tokenize(s.lower()) if not word in stop_words]
    
    # lemmatize    
    tokens =  [lemmatizer.lemmatize(word) for word in tokens]

    return tokens 

def build_model():
    
    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('moc',MultiOutputClassifier(RandomForestClassifier()))
    ])
    params = {
    'moc__estimator__n_estimators': [10],
    'moc__estimator__min_samples_split': [2, 3]
    }

    cv = GridSearchCV(pipeline, param_grid=params,verbose=10)
    return cv


def evaluate_model(model, X_test, Y_test, category_names):
    Y_pred = model.predict(X_test)
    for x in range(len(category_names)): 
        #precision_matrix = confusion_matrix(Y_test[x,:], Y_pred[x,:])
        #print(precision_matrix)
        print(classification_report(Y_test[:, x], Y_pred[:, x]))


def save_model(model, model_filepath):
    pickle.dump(model, open(model_filepath, 'wb'))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()