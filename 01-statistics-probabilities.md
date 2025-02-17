# Table of contents

1. [Statistics](#statistics)
2. [Probability](#probability)

## Statistics
There are two main branches of statistics - **descriptive** and **inferential**.
### Descriptive statistics
is concerned with summarizing a sample population in terms of indices such as mean, mode, standard deviation. It measures of **central tendencies** like mean, mode and median gives the most common occurrences in the data whereas measures of spread like variance, range, quartiles, standard deviation etc describe how far samples are from the central position. They are mainly used to organize, analyze and present data in a meaningful way.

#### Measures of Central Tendencies
<img width="434" alt="image" src="https://github.com/user-attachments/assets/13d389e1-a00d-4a37-aa77-2840db654cee" />

- **Mode**: Indicates the most likely value in the distribution, in other words, it is the most popular or frequently occuring value in the dataset.
- **Median**: the midway point between all values after they have been arranged in ascending or descending order. The midway point usually occurs at the 50% mark
- **The mean or arithmetic average**: is the ratio of the sum of all values to the number of values in the population.
<img width="455" alt="image" src="https://github.com/user-attachments/assets/2c853ebd-1dc8-43cf-adba-5c1b22726bd0" />

```py
import numpy as np  
from scipy import stats

dataset = np.array([3, 1, 4, 1, 1])

mean = np.mean(dataset)
print(mean) # 2.0

median = np.median(dataset)  
print('Median: {:.1f}'.format(median)) # Medial: 1.0

mode= stats.mode(dataset)  
print(mode)  
print('Mode: {}'.format(mode[0][0]))  
print('{} appeared {} times in the dataset'.format(mode[0][0], mode[1][0])) # 1.0 appeared 3 times in the dataset
# Mode is 1 because it's the most common number in our dataset.
```

#### Dispersion, Covariance and Correlation  
- The dispersion of a distribution refers to how widely spread sample data points are in that population. It explains the amount of variability present in a distribution, that is how widely do data points vary across across a central location.”

<img width="444" alt="image" src="https://github.com/user-attachments/assets/0543d503-bdf8-4eb0-b009-b9cec678e6ce" />

a. Distribution **A** has low dispersion. This is because most of its values are centered in the middle
b. Distribution **B** has greater dispersion as values appear to be located across a broader range.
c. Distribution **C** shows the most variation.

A or B and its height is very low indicating small values for measures of central tendency such as the mean. Some ways of **Statistical dispersion** is measured includes variance, standard deviation and interquartile range. <br />
Standard deviation formula

<img width="424" alt="image" src="https://github.com/user-attachments/assets/b73af820-06ea-449c-ae5e-d949f7c0ca9d" />

It should be noted that variance is the square of standard deviation which defines how much values of a variable are away from its mean. < br />

Covariance measures how well two random variables vary in line with each other. The covariance of X and Y tells us how much a change in X results in a corresponding change in Y. Covariance merely tells us whether variables are positively or negatively correlated so we use something called Correlation.

<img width="455" alt="image" src="https://github.com/user-attachments/assets/9802c2d7-9d84-430f-bad5-450bc5144cf1" />




#### inferential statistics
Is concerned with making predictions about a population through the study of a sample from that population. It discovers trends within a sample and then tries to generalize those trends to the wider population. 
It is made up of two parts, estimation of parameters and testing out hypothesis. The results of inferential statistics are usually presented as probabilities that show the confidence of particular parameters or events being true.

## Probability
