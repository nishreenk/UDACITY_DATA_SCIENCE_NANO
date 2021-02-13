import json
import plotly
import pandas as pd

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from flask import Flask
from flask import render_template, request, jsonify
from plotly.graph_objs import Bar
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier
from sqlalchemy import create_engine


app = Flask(__name__)

def tokenize(text):
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens

# load data
engine = create_engine('sqlite:///../data/DisasterResponse.db')
df = pd.read_sql_table('data/DisasterResponse.db', engine)

# load model
model = joblib.load("../models/classifier.pkl")


# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():
    
    # extract data needed for visuals
    # TODO: Below is an example - modify to extract data for your own visuals
    genre_counts = df.groupby('genre').count()['message']
    genre_names = list(genre_counts.index)
    #Category counts and Category Labels
    cc =df.drop(['id','message','original','genre'], axis=1).sum()
    cc=cc.sort_values(ascending=False)
    cats= list(cc.index)
    # 
    aid_related =df[df['aid_related']==1].groupby('genre').count()['aid_related']
    earthquake =df[df['earthquake']==1].groupby('genre').count()['earthquake']
    floods=df[df['floods']==1].groupby('genre').count()['floods']
    
    
    # create visuals
    
    graphs = [
        {
            'data': [
                Bar(
                    x=genre_names,
                    y=genre_counts
                )
            ],

            'layout': {
                'title': 'Distribution of Message Genres',
                'yaxis': {
                    'title': "Count"
                },
                'xaxis': {
                    'title': "Genre"
                }
            }
        },
        
        # bar graph of category distribution
        {
            'data': [
                Bar(
                    x=cats,
                    y=cc,               
                    marker=dict(color='rgba(194, 7, 106, 0.83)',
                    line=dict(color='rgba(74, 97, 156, 1.0)')
                    )
                   )
            ],
            'layout': {
                'title': 'Count of messages in each Category',
                'yaxis': {
                    'title': "Count of messages",
                    #'dtick':10,
                    'showexponent' :'last',
                    'exponentformat': 'e'
                },
                'xaxis': {
                    'title': "Category",
                    'tickangle': 45,
                    
                }
            }
        },
        
     # Barcharts of disaster and aid related tweets  
      {
            'data': [
                Bar(
                    x = genre_names,
                    y = genre_counts,
                    name='Total'
                    ),
                Bar(
                    x=genre_names,
                    y=aid_related,
                    text=aid_related,
                    textposition='auto',
                    name= 'Aid Related' 
                    
                    ),
                Bar(
                    x=genre_names,
                    y=earthquake,
                    text=earthquake,
                    textposition='auto',
                    name= 'Earthquake'
                    ),
                Bar(
                    x=genre_names,
                    y=floods,
                    text=floods,
                    textposition='auto',
                    name= 'Floods'
                    )],
                'layout': {
                'title': 'Tweets related to Aid, Earthquake and Floods',
                'yaxis': {
                    'title': "Count of tweets"                   
                    },
                'xaxis': {
                          'title': "Category",                                           
                         }
                },        
      } ]
    
    # encode plotly graphs in JSON
    ids = ["graph-{}".format(i) for i, _ in enumerate(graphs)]
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)
    
    # render web page with plotly graphs
    return render_template('master.html', ids=ids, graphJSON=graphJSON)


# web page that handles user query and displays model results
@app.route('/go')
def go():
    # save user input in query
    query = request.args.get('query', '') 

    # use model to predict classification for query
    classification_labels = model.predict([query])[0]
    classification_results = dict(zip(df.columns[4:], classification_labels))

    # This will render the go.html Please see that file. 
    return render_template(
        'go.html',
        query=query,
        classification_result=classification_results
    )


def main():
    app.run(host='0.0.0.0', port=3001, debug=True)


if __name__ == '__main__':
    main()