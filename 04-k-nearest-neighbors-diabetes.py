import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

dataset = pd.read_csv('./datasets/diabetes.csv')

dataset.head() # display first five records

print(dataset.shape) # get shape of dataset, number of observations, number of features

print(dataset.describe()) # get information on data distribution

# plot correlation between features
corr = dataset.corr() # dataframe correlation function
fig, ax = plt.subplots(figsize=(13, 13))

ax.matshow(corr) # color code the rectangles by correlation values

plt.xticks(range(len(corr.columns)), corr.columns) # Draw x tick marks
plt.yticks(range(len(corr.columns)), corr.columns) # Draw y tick marks

# Create features and labels
features = dataset.drop(['Outcome'], axis=1) # drop labels from dataset
labels = dataset['Outcome']

# split dataset intro training and test
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.25)

classifier = KNeighborsClassifier()
# fit data
classifier.fit(features_train, labels_train)
# Get predicted class labels
predictions = classifier.predict(features_test)

# get accuracy of model on test set
accuracy = accuracy_score(labels_test, predictions)
print(f"Accuracy: {accuracy}")