
**Project Components**

1. ETL Pipeline

 - Loads the messages and categories datasets

 - Merges the two datasets

 - Cleans the data

 - Stores it in a SQLite database

2. ML Pipeline

 - Loads data from the SQLite database

 - Splits the dataset into training and test sets

 - uilds a text processing and machine learning pipeline

 - Trains and tunes a model using GridSearchCV

 - Outputs results on the test set

 - Exports the final model as a pickle file

3. Flask Web App

 - Data visualizations using Plotly in the Flask web app. 


**Data**

Pre-labeled tweets and text messages from a real-life disaster is provided by Figure8
The data set contains real messages that were sent during disaster events. A machine learning pipeline categorizes these events so that one can send the messages to an appropriate disaster relief agency.
 
**HOW TO RUN INSTRUCTIONS**

1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
        
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.

    `python run.py`

3. Go to http://0.0.0.0:3001/
