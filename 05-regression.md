## Regression

The nature of regression problems is that we are trying to find **how the value of a dependent variable changes with respect to one or more independent variables.** In a nutshell, what we want to know is how much a  variable say y depends on a set of other variables say x, w such that we can learn to predict the value of y once we know the values of the variables it depends on.

Regression always produces a single value hence it is best applied to learning problems where we require a single real valued number. A good example is if we want to build a model that takes in information about a person such as their age, nationality, profession etc and we want to predict their expected income for a year. Our output would be a single value and regression would be well positioned to solve this problem.

**Introduction to labels and features**

**Supervised learning** as the name implies deals with teaching machine learning models with the help of data that is clearly labelled, that is data that has been annotated by a human to show what is to be learnt by the algorithm. The labels are regarded as the ground truth, the actual outcome that was observed from a particular data point.

**Unsupervised learning** does not include any labelled outcomes. The job of the algorithm is to learn from the raw data in order to come up with patterns which would provide insights on the data explored. The main difference is that there isn’t explicit feedback during training in the form of labelled examples. A famous application of unsupervised learning is in **clustering**. **Clustering** involves using a machine learning algorithm to categorize data points into groups (clusters) based on similarity of features.

### Features
A feature is a characteristic of an observed data point in a dataset. There may be more than one feature in a dataset. Features are usually measurable and represent a specific axis of explanation for the data. The quality of features selected has a direct impact on quality of models as models learn using features that are informative in order to arrive at a final prediction.  

Features that best describe the data should always be chosen as such features have a high discriminative tendency which helps the machine learning model classify outputs and predictions.  

A good approach is to always choose an optimum number of features, not too much as in such a case, many features would be uninformative which leads to overfitting of the model and not too little that the model underfits thereby failing to learn anything.  

**Principal Component Analysis (PCA)** is a dimensionality reduction technique which reduces the number of dimensions of our data to a small number that best describes its core features.


### Simple and Multiple Linear Regression  
Regression involves finding the relationship between variables. Regression is typically used for predicting a single real value given a bunch of predictors. In simple regression, there are only two variables. The first is the independent variable while the other is the dependent variable.

A straight line equation may be used to fit a set of data points to capture the relationship between both variables in simple regression.

<img width="421" alt="image" src="https://github.com/user-attachments/assets/0b6a764e-7fc2-4bf2-a66a-2f107dc4c607" />

The coefficient to be calculated is denoted by a while b is the intercept or bias of the model, x and y are the independent and dependent variables respectively.

In multiple linear regression, there are two or more independent variables, that is the number of predictors which determine the outcome y

<img width="409" alt="image" src="https://github.com/user-attachments/assets/f274ee25-613b-49d0-8cde-8d85c7c571f7" />

<br/>

<img width="423" alt="image" src="https://github.com/user-attachments/assets/1986d601-9988-4e05-ab1d-d82cf74a9309" />

**The coefficients** are the learnt parameters for each predictor.

**The mean square error** represents how far off our predictions are from the actual values.

**Variance score** is the coefficient of determination which gives the overall performance of the model. A variance score of 1 is a perfect model, so it is clear that with a score of 0.72, the model has learnt from the data.
