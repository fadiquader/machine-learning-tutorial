## Decision Trees and Random Forest

### The Entropy of a Partition  
**Entropy** can be defined as the measure of **uncertainty** in a sequence of **random events**. It is the rate of disorderliness in a sample space and is directly opposed to knowledge. When the entropy of a system is **high**, the knowledge that can be derived from the system is **low** and vice versa. An intuitive understanding of entropy is thinking of it as the amount of questions required to ask to arrive at some knowledge. For example, if I picked a random number and you were trying to guess what number it is. Asking a question like, “Is it an odd number”, reduces the possibilities space by half. This means that the entropy or the degree of uncertainty in trying to determine which number I choose is reduced. In the same vein, the amount of information gain is large because the question moved you closer to the answer by dividing the sample space. Entropy usually ranges from 0 to 1. A system with an **entropy of 0** is highly **stable** and the **knowledge** that can be derived from such a system is **high**. In general terms, **low** **entropy** in a system indicates **high** knowledge or instability.

<img width="422" alt="image" src="https://github.com/user-attachments/assets/f69dfaee-794c-4bd6-9fa7-3c1e86b2fe3a" />

The **entropy** of **two or more attributes **of a **classifier** is defined by:

<img width="423" alt="image" src="https://github.com/user-attachments/assets/c01fb40d-8c0e-4a5d-b69f-dd5b6dac7cd7" />

**Decision trees** are a machine learning algorithm that rely heavily on the **entropy** of an attribute and the information gain to determine how to **classify** samples in a classification problem. 


### Creating a Decision Tree  
A decision tree is a machine learning algorithm which is mainly used for **classification** that constructs a tree of possibilities where the branches in the tree represents **decisions** and the **leaves** represents **label** classification. The purpose of a decision tree is to create a structure where samples in each branch are **homogenous** or of the same type. It does this by splitting samples in the training data according to specific attributes that increase homogeneity in branches. These attributes form the decision node along which samples are separated. The process continues until all sample are correctly predicted as represented by the leaves of the tree.

<img width="472" alt="image" src="https://github.com/user-attachments/assets/69d578bb-639d-4853-8e88-59ebe119dfa9" />

**Age** is the attribute that offers the most information gain so samples are split on that decision node.

**The information gain** is closely **related** to the **entropy** and is defined as the difference in entropy of the targets (final entropy) and the entropy given a particular attribute was chosen as the root node.

<img width="422" alt="image" src="https://github.com/user-attachments/assets/3d1754a0-d95b-44c0-9e7f-9e48928804d0" />

The formula above is used to calculate the decrease in entropy. The attribute with the largest information gain or decrease in entropy is chosen as the root node.


## Random Forests  
Random forests are a type of **ensemble model**. An ensemble model is one which is constructed from other models. This means that it is a combination of several weak learners to form a strong learner. The prediction of an ensemble model may be the average or weighted average of all learners that it is comprised of.  
       
Random forests are an extension of decision trees whereby several decision trees are grown to form a forest. The final prediction of a random forest model is a combination of all component decision trees. For regression it may be a simple average of outputs or a label vote in the case of classification. Though random forest are made of several decision trees, each decision tree is trained on a subset of data (bagged data which is around 60% of the entire dataset) that is randomly selected hence the name random forest. The other trick of random forest is that unlike a decision tree where the best attribute is chosen in order to split samples at a decision node from all available attributes, random forest only picks the best attribute from a subset of randomly chosen attributes for each decision node. As a result, each node in a tree is not deterministic, that is for each time we run the algorithm, we are likely to end up with different tree structures.

<img width="425" alt="image" src="https://github.com/user-attachments/assets/f6c92757-5af1-4da2-82a6-8fb2e992f286" />

The tree is made up of several trees trained on different instances of the dataset. The attributes in each decision node are also randomized. Finally, the output prediction is an ensemble of the classification of each decision tree.


