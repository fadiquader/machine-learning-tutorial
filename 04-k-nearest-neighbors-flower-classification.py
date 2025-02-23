import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import scipy as sp

dataset = pd.read_csv('./datasets/Iris.csv')

dataset.head()

x = dataset.iloc[:, 1:5].values # select features ignoring non-informative column id
y = dataset.iloc[:, 5].values # species contains targets for our modal

le = LabelEncoder()
# transform label names into categorical values
y = le.fit_transform(y) # [0, ..1, ..2]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)

classifier = KNeighborsClassifier(n_neighbors = 3)

# fitting modal
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy}")