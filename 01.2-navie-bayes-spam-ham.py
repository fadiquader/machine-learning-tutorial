import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv('./datasets/spam.csv', encoding="ISO-8859-1")

data.head() # display first five records

count_class = pd.Series(data['v1']).value_counts(sort=True) # ham 4825, span 747
print(count_class)

count_class.plot(kind='bar', color=['blue', 'red'])
plt.title('Spam Class Distribution')
plt.show()

# words can't be fed into the model so we need to vectorize them to create new features
f = CountVectorizer(stop_words='english') # stop words are like "the", "a", "of" so we need to remove them
X = f.fit_transform(data['v2'])
print(np.shape(X))
# After vectorization, 8,404 features are created

# Map our target variables into categories and split the dataset into train and test sets.
data["v1"] = data["v1"].map({ 'spam': 1, 'ham': 0 })

X_train, X_test, y_train, y_test = train_test_split(X, data['v1'], test_size=0.25, random_state=42)

# init Naive Bayes Algorithm
clf = MultinomialNB()
clf.fit(X_train, y_train)

# gauge model performance on the test set
score = clf.score(X_test, y_test)

print(f"Accuracy: {score}")