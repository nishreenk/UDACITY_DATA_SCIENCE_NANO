This is the Model Pipeline for NLP to process text data. 


The script uses a custom tokenize function using nltk to case normalize, lemmatize, and tokenize text. 
This function is used in the machine learning pipeline to vectorize and then apply TF-IDF to the text.
The pipeline processes text and then performs multi-output classification on the 36 categories in the dataset. 
GridSearchCV is used to find the best parameters for the model.
The TF-IDF pipeline is only trained with the training data. 
The f1 score, precision and recall for the test set is outputted for each category.
