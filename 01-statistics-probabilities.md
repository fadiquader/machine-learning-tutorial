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
- The dispersion of a distribution refers to how widely spread sample data points are in that population. It explains the amount of variability present in a distribution, that is how widely do data points vary across across a central location.

<img width="444" alt="image" src="https://github.com/user-attachments/assets/0543d503-bdf8-4eb0-b009-b9cec678e6ce" />

- Distribution **A** has low dispersion. This is because most of its values are centered in the middle
- Distribution **B** has greater dispersion as values appear to be located across a broader range.
- Distribution **C** shows the most variation.

A or B and its height is very low indicating small values for measures of central tendency such as the mean. Some ways of **Statistical dispersion** is measured includes variance, standard deviation and interquartile range. <br />
Standard deviation formula

<img width="424" alt="image" src="https://github.com/user-attachments/assets/b73af820-06ea-449c-ae5e-d949f7c0ca9d" />

It should be noted that variance is the square of standard deviation which defines how much values of a variable are away from its mean. <br />

Covariance measures how well two random variables vary in line with each other. The covariance of X and Y tells us how much a change in X results in a corresponding change in Y. Covariance merely tells us whether variables are positively or negatively correlated so we use something called Correlation.
example: as study hours increase, exam scores also increase

<img width="455" alt="image" src="https://github.com/user-attachments/assets/9802c2d7-9d84-430f-bad5-450bc5144cf1" />


The correlation is defined as the covariance normalized (divided) by the square root of the product of the variance of each random variable.

<img width="427" alt="image" src="https://github.com/user-attachments/assets/5c926ed4-2db7-458f-a943-5e1397bb7c19" />

The values for correlation lies in the range -1 to 1. With 1 indicating that there is positive correlation between variables and -1 indicating negative correlation.

<img width="415" alt="image" src="https://github.com/user-attachments/assets/b75eef85-cbb0-43f8-8a1a-1ce99132db69" />

```py
import numpy as np

x = np.random.normal(size=2)  
y = np.random.normal(size=2)
   
z = np.vstack((x, y)) # We stack x and y vertically to produce z using the line of code below.  
c = np.cov(z.T)  
print(c) # [[0.0865..., 0.0200...], [..., ...]]

# correlation
from scipy.stats.stats import pearsonr     
a = [1,4,6]
b = [1,2,3]  
corr = pearsonr(a,b)  
print(corr) # (0.99.., 0.073...)
```

#### inferential statistics
Is concerned with making predictions about a population through the study of a sample from that population. It discovers trends within a sample and then tries to generalize those trends to the wider population. 
It is made up of two parts, estimation of parameters and testing out hypothesis. The results of inferential statistics are usually presented as probabilities that show the confidence of particular parameters or events being true.

## Probability
### Dependence and Independence  
Probability is a measure of how likely we feel an event would occur. Probability is therefore a measure of likelihood. It is usually a value between 0 and 1 with 0 indicating impossibility, that is the event would never occur and 1 means certainty, the event is sure to occur. <br/>
In probability, two events are said to be **dependent** if the occurrence of the first event directly affects the probability of the second event occurring. An example of dependent events are writing a book and getting published. To get published, you must first write a book. The probability of getting published directly depends on writing a book. The order is important as it cannot be changed. Writing a book must occur first before any publication. <br />

**Independent** events are those events whose probability of occurrence are not dependent on each other. The fact that a first event has occurred does not in any way mean that a second event would occur or not. Both events are not linked as they are independent. To determine whether two events are independent, we first ask ourselves if both events can happen in any order. If the answer is yes, we ask ourselves a second question, does one event affect the outcome of the other. If the answer is no, then we have been able to prove that both events are completely independent of each other. An example of independent events are buying a new phone and eating your favorite meal. Those events are not dependent on each other. It is possible to imagine them occurring in any order. The fact that you just bought a new phone does not in any way affect the probability of you eating your favorite meal. 

For two independent events lets say A and B. The probability of event A occurring given that event B has occurred is equal to the probability of A.  
       
P(A|B) = P(A)  

P(B|A) = P(B)  
       
What this means is that whether or not event B has occurred, it does not affect the probability of A occurring because the probability of A is only dependent on itself, that is event A does not depend on external events.

The probability of two independent events occurring is equal to the product of their individual probabilities.  
       
P(A∩B) = P(A)·P(B)

### Conditional Probability  
The measure of the probability of an event, say A occurring, given the knowledge that another event, say B, has occurred. Conditional probability deals with the probability of occurrence of an event in relation to other events. To define this formally, the probability of A given B is equal to the probability of the intersection of A and B (that is both events occur) divided by the probability of B.  
       
P(A|B) = P(A∩B)/P(B)  

P(A|B) means probablity of A given B

Formula:
The formula for conditional probability is:

P(A | B) = P(A and B) / P(B)

This reads as:

P(A | B): "The probability of A happening given that B has happened."
P(A and B): "The probability that A and B happen together."
P(B): "The probability that B happens."

### Random Variables  
The types of variables whose values are given by random processes. What this means is random variables maps the outcome of a random process to numbers that can be used in probability theory. An example of a random process is throwing a dice. The outcome is clearly random and cannot be predetermined. However, we can assign numbers to those random outcomes, the numbers so assigned would be quantities of a random variable. Random variables are also measurable and contain numbers like regular variables in algebra but the key difference is that they are produced by a random process.

P(getting a number greater than 3 after rolling a dice once)  

But if we define the random process using random variables, the notation can be simplified greatly:  
       
X = getting a number greater than 3 after rolling a dice once  
       
P(X > 3)

### Bayes’ Theorem and Naive Bayes Algorithm
Using Bayes’ theorem we can calculate the probability of an event A, given event B occurred, as the product of probability of B given A and the probability of A all divided by the probability of B.  

P(A|B) = P(B|A)P(A)/P(B)

**The Key Idea:**
You start with an initial belief about the probability of something (called the "prior").
Then, you get new evidence.

Bayes’ theorem helps you combine the prior with the new evidence to get an updated probability (called the "posterior").

**Example**:

Say we draw a single card from a deck of playing cards, what is the probability that the card so drawn is a king, given evidence (additional information) whether it is a face card.  
       
First let us define define Bayes theorem in line with the question.  
       
P(King|Face) = P(Face|King)P(King)/P(Face)  
       
Where;  
       
P(King|Face) = probability the card is a king given it is a face card  
       
P(Face|King) = probability the card is a face card given it is a king = 1 because all kings are face cards (contains a face).
       
P(King) = probability the card is a king  is 4 / 52 = 1 / 3
       
P(Face) = probability the card is a face card ( 4 face types * 3 cards jack, queen, and king)) 12 / 52 = 3 / 13

P(King|Face) = (1/13)(1)/(3/13) = 1/3

### Naive Bayes algorithm 
Is an application of Bayes’ theorem as a classification algorithm with the explicit assumption that all features or predictors are independent.

It's called "naive" because it makes a big assumption: it assumes that all features (variables) are independent of each other, which is often not true in real life. Despite this, it works surprisingly well in many situations.

**What does it do?**

It predicts the class of an item given its features.
It calculates the probability of each class and picks the one with the highest probability.

**Formula:**

P(Class | Features) = [P(Features | Class) * P(Class)] / P(Features)
