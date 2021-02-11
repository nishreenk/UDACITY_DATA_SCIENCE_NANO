
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
 
