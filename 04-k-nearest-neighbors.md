## K-Nearest Neighbors

Nearest neighbor algorithm is an algorithm that can be used for regression and classification tasks but is usually used for classification because it is simple and intuitive.

At training time, the nearest neighbor algorithm simply memorizes all values of data for inputs and outputs. During test time when a data point is supplied and a class label is desired, it searches through its memory for any data point that has features which are most similar to the test data point, then it returns the label of the related data point as its prediction.

## Simplified Explanation

1. **Training Phase**:
   - KNN doesn’t really “train” in the traditional sense. Instead, it memorizes the entire training dataset.
   - For example, imagine you have a dataset of fruits with features like weight and color, and you want to classify them as apples or oranges.

2. **Prediction Phase**:
   - When you want to predict the class of a new, unknown data point:
     1. **Calculate Distances**: Measure the distance between the new data point and all the points in the training dataset. Common distance metrics include Euclidean distance.
     2. **Find Nearest Neighbors**: Identify the K nearest neighbors (data points) based on the calculated distances.
     3. **Vote or Average**:
        - For classification: The majority class among the K nearest neighbors is chosen as the prediction.
        - For regression: The average of the values of the K nearest neighbors is used as the prediction.

## Example: Classifying Fruits

### Dataset

| Fruit | Weight (grams) | Color (Redness Scale) | Class (Apple/Orange) |
|-------|----------------|-----------------------|----------------------|
| A     | 150            | 7                     | Apple                |
| B     | 200            | 3                     | Orange               |
| C     | 180            | 6                     | Apple                |
| D     | 220            | 2                     | Orange               |

### Prediction

You want to classify a new fruit with weight 170 grams and color 5.

1. **Calculate Distances**:

<img width="473" alt="image" src="https://github.com/user-attachments/assets/6e246dc9-682b-4040-9837-e2b9474a3436" />

<img width="676" alt="image" src="https://github.com/user-attachments/assets/53c20d51-9dc5-40ad-8476-6ab467512354" />


3. **Find Nearest Neighbors**:
   - Let’s choose \(K=2\). The two nearest neighbors are:
     - C (distance 10.0, class Apple)
     - A (distance 20.1, class Apple)

4. **Vote**:
   - Both nearest neighbors are classified as Apple. Therefore, the new fruit is classified as an Apple.

## Example: Predicting House Prices (Regression)

### Dataset

| House | Size (sq ft) | Bedrooms | Price (\$) |
|-------|--------------|----------|-----------|
| A     | 2000         | 3        | 300,000   |
| B     | 2500         | 4        | 400,000   |
| C     | 1800         | 2        | 250,000   |
| D     | 3000         | 5        | 500,000   |

### Prediction

You want to predict the price of a house with size 2200 sq ft and 3 bedrooms.

1. **Calculate Distances**:
<img width="666" alt="image" src="https://github.com/user-attachments/assets/fbfeb9bc-dbbf-4c34-a370-2d4f3707e574" />

2. **Find Nearest Neighbors**:
   - Let’s choose \(K=2\). The two nearest neighbors are:
     - A (distance 200, price \$300,000)
     - B (distance 300, price \$400,000)

3. **Average**:
<img width="674" alt="image" src="https://github.com/user-attachments/assets/ced1a891-8e55-4663-93e3-381a9d33906b" />

So, the predicted price for the new house is \$350,000.

### References: 
- k nearest neighbor (kNN): how it works https://www.youtube.com/watch?v=k_7gMp5wh5A
