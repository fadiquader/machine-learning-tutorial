<img width="520" alt="image" src="https://github.com/user-attachments/assets/7fb12d92-0bcf-4d09-98e6-5a3b4271650a" />

### Data Acquisition  
Immediately after we settle on a research goal, the next step is to acquire appropriate data through which we can begin to derive insights. The kind of data that is acquired is tailored towards the kind of problem we want to solve. By getting that particular type of data, we are making an assumption that the solution space provided by the data contains answers to our questions.

Data may come from relational databases, spreadsheets, inventories, external APIs etc. During this stage, it is reasonable to check that the data is in the correct format for our purposes. 

### Data Preparation  
Data preparation involves three main mini-steps. Data cleansing, data transformation and data combination. It changes the raw data which was obtained from the real world to a form where it can be read and analyzed by a computer, in this case a machine learning algorithm.

First, we clean the datasets we have obtained. This is usually done by identifying missing values, errors, outliers etc.

Data transformation is centered on aggregating data, dealing with categorical variables, creating dummies to ensure consistency, reducing the number of variables in order to retain the most informative features and discard redundant features, scaling the data etc. Scaling is important as features may originally be in different ranges and to get better performance, it is often sensible to bring all variables to a common range.

### Data Exploration  
The data exploration stage is concerned with looking closely at the data to get a better sense of what the data is all about. This step involves using statistical metrics such as mean, median, mode, variance etc.

Some common visualization techniques used in exploratory data analysis phase includes, bar charts, pie charts, histograms, line graphs, box plots etc.”

<img width="470" alt="image" src="https://github.com/user-attachments/assets/c9ab3d1c-adbe-45c4-a6a8-9a0decc00ee6" />

### Data Modelling  
In the data modelling step we take a more involved approach when accessing the data. Data modelling involves choosing an algorithm, usually from the related fields of statistics, data mining or machine learning. Deciding which features should go into the algorithm as the input, executing the model and finally evaluating the trained model for performance.

Before feeding in data to any model, we first chose the most important features as inputs to the model. What that means is that we would give preference to features that contain underlying properties that enables our model learn its task better, whether that is classification or regression. Those features which do not drive the final prediction or are uninformative are dropped. Techniques such as **Principal Component Analysis (PCA)** can be used.

The next step involves choosing an appropriate algorithm for the learning task. Different algorithms are better suited to different learning problems. Logistic regression, Naive Bayes classifier, Support Vector Machines, decision trees and random forests are some popular classification algorithms with good performance.

In order to be able to support experimentation without biasing our models in the process, we adopt an evaluation scheme. We divide the data into three sections known as splits. The three splits are train, validation and test sets. The train split is used for training the model while the validation split is used for hyperparameter tuning. Hyperparameter tuning means adjusting the hyperparameters (input options) available to an algorithm and checking its performance on the validation set to see whether the adjusted hyperparameter had a positive effect or not. Hyperparameter tuning is done on the most promising models to further improve performance. Finally, the trained model is evaluated on the test set which was not used for training or validation. In other words, the model has never seen the data contained in the test set. This provides an unbiased assessment of the model as we can observe its generalization to new data.

The evaluation metric on the train and validation splits enable us to debug the model to discover whether it is underfitting or overfitting to the training set. If it is underfitting (not learning enough), we can increase the power of the model else we apply regularization if it is overfitting (learning noise).

### Data Presentation  
The purpose of this step is to communicate the insights discovered from the data science process in such a way that the information provided is actionable. This means data presentation should enable a decision making process. It should be clear from the presentation what steps need to be taken to solve the original problem which was posed as a question in the first step.

