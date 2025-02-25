import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

dataset = pd.read_csv('./datasets/wine.csv')

features = dataset.drop(['Wine'], axis=1)
labels = dataset['Wine']

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.25)

# Training the model
classifier = RandomForestClassifier()
classifier.fit(features_train, labels_train)

# Evaluate the model
pred = classifier.predict(features_test)

accuracy = accuracy_score(labels_test, pred)
print(f"Accuracy: {accuracy}")