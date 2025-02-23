## Logistic Regression
Logistic Regression is a classification algorithm. It's used when the dependent variable is binary in nature, that is when it can be either one of two values (categories) example true or false. It is a linear combination of weighted input features applied to the sigmoid function. The logit or sigmoid function is at the heart of logistic regression and models data along the range of 0 to 1.

<img width="432" alt="image" src="https://github.com/user-attachments/assets/66d339d3-e690-46c6-81e9-1fb9a234e195" />

<img width="604" alt="image" src="https://github.com/user-attachments/assets/c2c7efc2-c5a0-4a89-9c71-a68ad75104ee" />

<img width="603" alt="image" src="https://github.com/user-attachments/assets/38965344-87c8-476a-ad2f-584a0c05c5f3" />

<img width="603" alt="image" src="https://github.com/user-attachments/assets/6dde6487-6aff-4c09-adca-cf568b05c0e1" />

<img width="603" alt="image" src="https://github.com/user-attachments/assets/8fa95376-c28a-4962-9c76-3b6603eda278" />

### Logistic Regression Cost Function (Binary Cross-Entropy)
https://github.com/EyasuTew/machine-learning-1/blob/master/week3/logistic-regression-model.md 

To train a logistic regression model, we need to measure how well the model is doing and **optimize the model parameters** (weights and biases). This is where the **cost function** comes into play.

For logistic regression, the **cost function** is based on the concept of log loss (also known as binary cross-entropy). The cost function measures the difference between the predicted probabilities and the actual labels.

**Logistic Regression Cost Function:**

<img width="604" alt="image" src="https://github.com/user-attachments/assets/40d54711-d492-49ea-b09c-445dd0ff58d7" />

<img width="604" alt="image" src="https://github.com/user-attachments/assets/f6d2faf1-dd02-4039-ab20-1c806963ab15" />


### Total Cost (Log-Loss)
The total cost (or log-loss) for all the training examples is simply the average of the cost function calculated for each individual example. Mathematically:

<img width="602" alt="image" src="https://github.com/user-attachments/assets/84817716-0a40-4f5b-9c3c-8d6b92c30ee5" />

<img width="598" alt="image" src="https://github.com/user-attachments/assets/da9d0265-21db-4d0a-b5dc-4fe068db2162" />

