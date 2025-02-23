import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

dataset = pd.read_csv('./datasets/HousingData.csv')
# Remove rows with missing values
dataset.dropna(inplace=True)
# print(dataset.head())

plt.scatter(dataset['CRIM'], dataset['MEDV'])
plt.xlabel('Per capita crime rate by town')
plt.ylabel('Price')
plt.title("Prices vs Crime rate")
# Price drops as the crime rate in the neighborhood increases
plt.show()

X = dataset.drop('MEDV', axis=1)
y = dataset['MEDV']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

# The Coefficients
print(f"Coefficients: {regressor.coef_}")
# Mean squared error
print(f"Mean squared error: {mean_squared_error(y_test, y_pred)}")
# Variance score: 1 is perfect
print(f"Variance Score: {r2_score(y_test, y_pred)}")

plt.scatter(y_test, y_pred)
plt.ylabel("Predicted prices: $\hat{Y}_i$")
plt.title("Prices vs Predicted prices $\hat{Y}_i$")
plt.show()