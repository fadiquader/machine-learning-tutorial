
### What is Machine Learning?
Machine learning at its simplest form is all about making computers learn from data by improving their performance at a specific task through experience. Similar to the way humans learn by trying out new things and learning from the experience, machine learning algorithms improve their capability by learning patterns from lots of examples.

There are three main branches of machine learning namely - supervised learning, unsupervised learning and reinforcement learning. In some cases a fourth branch is mentioned - semi-supervised learning but this is really just a special instance of supervised learning.

### Supervised Learning Algorithms
Supervised learning is by far the most common branch of machine learning. Supervised learning algorithms are those machine learning algorithms which are trained with **labelled** examples. It would be remembered that we defined machine learning as making algorithms that learn from data (examples) without being explicitly programmed. The main intuition to understand when dealing with supervised learning algorithms is that, they learn through the use of examples that are clearly annotated to show them what they are supposed to learn. The algorithms therefore try to find a mapping representation from inputs to outputs using the labels as a guide. The two main applications of supervised learning algorithms are classification and regression
       
Classification involves training a learning algorithm to correctly separate examples into predefined categories or classes. A popular example of classification is spam detection where an email is correctly identified to belong to one of two classes - spam or not spam.

Regression is a learning problem where the algorithm is interested in predicting a single real value number. Regression is used where a single numeric entity is to be predicted. An example of regression would be predicting the age of a person given a profile picture or predicting the salary of an individual given information about the individual such as level of education, work experience, age, country of residence etc.

Supervised learning algorithms are easier to train when compared to unsupervised or reinforcement learning algorithms. This is because the presence of labels simplify the learning problem since there exist a clear way of determining performance during training. However, it should be noted that most supervised learning problems can also be modelled as unsupervised if we get rid of labels. Datasets for supervised learning are more expensive to acquire as it requires meticulous human annotation of examples. 

### Unsupervised Learning Algorithms  
Unsupervised learning involves learning directly from raw data. This type of learning takes place without the presence of a supervisor in the training loop in form of labels. Unsupervised learning algorithms are free to explore the underlying data distribution and come up with patterns that best describe the entire dataset. The training process is not guided by humans through labelled examples and as such unsupervised learning algorithms are more powerful as they can discover patterns which domain experts may not have thought of. Unsupervised learning algorithms merely use the data distribution or its latent (hidden) representations to unearth insights which may be in the form clusters, groups or distributions.  
       
There are many applications of unsupervised learning algorithms such as clustering, dimensionality detection, generative models etc.

**Clustering** is one of the popular implementations of unsupervised learning. It involves the automatic discovery of groups (clusters) of data points from raw data. Members of a group share similar features, that is they are alike. An example of clustering would involve grouping customers of a tv streaming service into the type of shows that they watch. Users with similar interests would generally be found in the same group. 

**Dimensionality reduction** is a machine learning technique that reduces the number of attributes (features) fed in a model to only the most relevant ones which drive predictions. It has been observed empirically, that models with greater number of features or dimensions perform worse on generalization. **Principal component Analysis (PCA)** is probably the most popular dimensionality reduction technique and is an example of an unsupervised learning algorithm. PCA reduces the dimensions of data by identifying those axes that contain the most variability. What that means is that it discovers principal components which offer the most discriminative features.

Generative models are another popular instance of unsupervised learning algorithms. They have made recent headlines because of their ability to artificially generate photographs and works of art that look realistic. Generative Adversarial Networks (GANs) currently produce state of the art results across many image generation benchmarks and are among the most popular examples of generative models.


### Semi-supervised Learning Algorithms 
In semi-supervised learning, while there isn’t an explicit label, there exist an implicit heuristic which serves as a supervisor in the training loop. Semi-supervised models do not contain any external source of labels but only rely on input features. However, the learning task is set up in such a way that supervision still takes place in the form of“extraction of pseudo-labels from inputs through a heuristic algorithm. A popular example of semi-supervised learning algorithms are autoencoders.

<img width="392" alt="image" src="https://github.com/user-attachments/assets/8e3460be-bf06-4754-92f5-4dedff4d5d70" />

The learning task is to **reduce the dimensions** of the input into a smaller latent space representing the most important hidden features, then **reconstruct the input** from this lower dimensional space. So given an input, example an image, an autoencoder shrinks the image into a smaller latent representation that still contains most of the information about the image, then reconstructs the original input image from this low dimensional space. Even if there are no explicit labels, it would be observed that the input serves as the supervisor since the learning task is to reconstruct the input.

The first part of the network that reduces the dimensions of the input is called an encoder while the second part that scales the encoded features back to the full size input is called the decoder.

### Reinforcement Learning Algorithms
In reinforcement learning there are three main components, an **agent**, an **environment** and **actions**. The goal of reinforcement learning is to train an intelligent agent that is capable of navigating its environment and performing actions that maximizes its chances of arriving at some end goal. Actions carried out by the agent change the state of the environment and **rewards** or **punishment** may be issued based on the actions taken by the agent. The challenge is for the agent to maximize the accumulated rewards at the end of a specific period so that it can actualize an end goal (objective).  

<img width="505" alt="image" src="https://github.com/user-attachments/assets/bb187fd7-b600-4de8-862b-1974ae5f368e" />

An agent (the reinforcement learning) interacts with the world (environment) through actions. The environment provides observations and rewards to the agent based on the kind of action taken by the agent. The agent uses this feedback to improve its decision making process by learning to carry out actions associated with positive outcomes.

### Overfitting and Underfitting
Generalization in a nutshell deals with how well a trained machine learning model would perform on new data which it has not seen, that is data it was not trained on. In other words, how well can a model generalize the patterns it learnt on the training set to suit real world examples, so that it can achieve similar or better performance.

We say a model has **overfit** to a training set when it has failed to learn only useful representations in the data but has also adjusted itself to learn noise and outliers in order to get an artificially high training set accuracy.

#### Noise and Outliers
**Noise:**

**Definition:** Noise refers to random errors or fluctuations in the data. It is the part of the data that does not contain useful information for making predictions.

Example: Imagine you are measuring the temperature every hour. The actual temperature might be 75°F, but your thermometer might read 75.1°F or 74.9°F due to measurement errors. These small variations are noise.

**Outliers:**

**Definition:** Outliers are data points that are significantly different from the rest of the data. They can occur due to variability in the data or experimental errors
.
Example: In a dataset of house prices, most houses might be priced between $200,000 and $500,000. However, one house might be priced at $10 million because it is a luxury mansion. This $10 million house is an outlier.


**Underfitting** means that the model has not used the information available to it but has only learnt a small subset of representations and has thrown away majority of useful information, thereby making it to make unfounded assumptions.

The ideal situation is to find a model that neither underfitts nor overfitts but exhibits the right balance between optimization and generalization. This can be done by maintaining a third set of examples known as **the validation set**. The validation set is used to tune (improve) the performance of the model without overfitting the model to the training set. Other techniques for tackling overfitting includes applying **regularization** which punishes more complicated models and acquiring more training examples. Underfitting can be stymied by increasing the capacity of the learning algorithm so that it can take advantage of available features.

<img width="420" alt="image" src="https://github.com/user-attachments/assets/00c51141-2a36-4f84-bd8b-df6eac51688d" />

The plots above show three simple line based classification models. The first plot separates classes by using a straight line. The straight line model is clearly underfitting as it has failed to use majority of the information available to it to discover the inherent data distribution.

The second plot shows an optimal case where the optimization objective has been balanced by generalization criterion. Even though the model misclassified some points in the training set, it was still able to capture a valid decision boundary between both classes.

The last plot illustrates a case of overfitting. The decision boundary is convoluted because the classifier is responding to noise by trying to correctly classify every data point in the training set. The accuracy of this classifier would be perfect on the training set but it would perform horribly on new examples because it optimized its performance only for the training set.

### Correctness
The evaluation metric chosen depends on the type of learning problem. Accuracy is a popular evaluation metric but it is not suitable for all learning problems. Other measures for evaluation include recall, precision, sensitivity, specificity, true positive rate, false positive rate etc. The evaluation used should be in line with the goals of the modelling problem.

The dataset should be divided into train, validation and test splits. The model is trained on the training set, the validation set is reserved for hyperparameter tuning for best performing models and the test set is only used once at the conclusion of all experimentation.  

A **confusion matrix** is widely used as a simple visualization technique to access the performance of classifiers in a supervised learning task. It is a table where the rows represent the instances in the actual class (ground truth) while the columns represents predictions. The order may be reversed in some cases. It is called a confusion matrix because it makes it easy to see which classes the model is misclassifying for another, that is which classes confuse the model

<img width="463" alt="image" src="https://github.com/user-attachments/assets/0b5c46c8-3af2-40c9-9589-82fde0161ccd" />

### The Bias-Variance Trade-off
The bias of a model is defined as the assumptions made by the model to simplify the learning task. A model with **high bias** makes assumptions which are not correlated by the data. This lead to errors because predictions are usually some way off from actuals. Variance on the other hand is how susceptible a model is to noise in the training data.

A good machine learning algorithm should strive to achieve **low bias and low variance**. Bias and variance are related to overfitting and underfitting earlier encountered. A model with **high bias is underfitting** the training data because it has made simplistic assumptions instead of learning from information available. Similarly, a model with **high variance** is **overfitting**, because it has modelled noise and as a result, its performance would vary widely across the training set, validation set and test set.

<img width="410" alt="image" src="https://github.com/user-attachments/assets/d81d3ae2-5c2d-4cb7-a0e4-587b56a8a5b7" />


