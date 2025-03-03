## Classification
A class or label can be understood as a category that represents a particular quantity, therefore what classification algorithms do is to identify the category that an example fits into. If the classification problem is posed in such a way that there are two distinct classes, we have a binary classification problem. In a case where we have more than two classes (labels), the learning problem is referred to as multi-class classification indicating that observations could fall into any of the n classes. 

## Support Vector Machine
Support vector machines also known as support vector networks is a popular machine learning algorithm used for classification. The main intuition behind support vector machines is that it tries to locate an optimal hyperplane which separates data into correct classes making use of only those data points close to the hyperplane. The data points closest to the hyperplane are called support vectors.  

There may be several hyperplanes that correctly separates classes but support vector machine algorithm chooses the hyperplane that has the largest distance (margin) from the support vectors (data points close to the hyperplane). The benefit of selecting a hyperplane with the widest margin is because this reduces the chance of mistakenly misclassifying a data point during test time 

<img width="419" alt="image" src="https://github.com/user-attachments/assets/07d7e60f-59a2-4d00-b78d-11d75972e2b7" />

