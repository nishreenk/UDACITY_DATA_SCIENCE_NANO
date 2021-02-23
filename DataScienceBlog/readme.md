**Therabank Personal Loan Marketign Campaign**

**Data Description:**

_Bank_Personal_Loan_Modelling.csv_ is the dataset filename.

The dataset contains data on 5000 customers. The data include customer demographic information (age, income, etc.), the customer's relationship with the bank (mortgage, securities account, etc.), and the customer response to the last personal loan campaign (Personal Loan). Among these 5000 customers, only 480 (= 9.6%) accepted the personal loan that was offered to them in the earlier campaign.

**Domain:**

Banking


**Context:**

This case is about a bank (Thera Bank) whose management wants to explore ways of converting its liability customers to personal loan customers (while retaining them as depositors). A campaign that the bank ran last year for liability customers showed a healthy conversion rate of over 9% success. This has encouraged the retail marketing department to devise campaigns with better target marketing to increase the success ratio with a minimal budget.

Feature Information:
- ID: Customer ID
- Age: Customer's age in completed years
- Experience: #years of professional experience
- Income: Annual income of the customer ($000)
- ZIP Code: Home Address ZIP code.
- Family: Family size of the customer
- CCAvg: Avg. spending on credit cards per month ($000)
- Education: Education Level. 1: Undergrad; 2: Graduate; 3: Advanced/Professional
- Mortgage: Value of house mortgage if any. ($000)
- Personal Loan: Did this customer accept the personal loan offered in the last campaign?
- Securities Account: Does the customer have a securities account with the bank?
- CD Account: Does the customer have a certificate of deposit (CD) account with the bank?
- Online: Does the customer use internet banking facilities?
- Credit card: Does the customer use a credit card issued by the bank?


**Outcomes:**
- Exploratory Data Analysis
- Preparing the data to train a model
- Training and making predictions using a classification model
- Model evaluation using Recall, ROC and F1 score metrics


**Objective:**
The classification goal is to predict the likelihood of a liability customer buying personal loans.

**Steps taken:**

1. Import the datasets and libraries(Pandas , Numpy, Matplotlib, SKLearn and Seaborn)
 
2. EDA: Study the data distribution in each attribute and target variable, sharing insights
 
- Number of unique in each column
 
- Number of people with zero mortgage

- Number of people with zero credit card spending per month
 
- Value counts of all categorical columns

- Univariate and Bivariate Analysis of the data

3.  Prepare the model inputs
  
- Converting categorical varaibles

- Dropping columns that are correlated, or are irrelevant to the study

- Split the data into training and test set in the ratio of 70:30 respectively 

4. Use Logistic Regression models('newton-cg','lbfgs','liblinear','sag', and 'saga’)  to predict whether the customer will take personal loan or not. 
Show all the metrics related for evaluating the model performance. The best performing model Newton-cg was picked, and finetuned. Predictions were made ont he test set with this model. The testing score = 0.965. The ROC-AUC score = 0.86. Recall = 0.72, F1-score = 0.81. 

 - Fine tune model parameters of Logistic Regression model chosen 
  
 **How does the Model Predict for the Marketing campaign** 
 The bank wants to give loan to the people who are eligible for the Personal loan. i.e. People who are eligible (1) should not be predicted incorrectly(0) else the marketing team will lose money. The model is optimized for a smaller number of False Positives. If the number of False positives is high the marketing department will lose money targeting the wrong customers. The final testing score is 0.965 implying that our model can predict about 96.5% of the predictions correctly.
 
 **Acknowledgemet**
 
 UT Austin, Austin, Texas 
 
 Great Learning, AIML PGP
