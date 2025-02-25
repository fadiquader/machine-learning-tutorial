## Neural Networks
### Perceptrons  
The perceptron is a binary linear classifier that is only capable of predicting classes of samples if those samples can be separated via a straight line. **The perceptron algorithm** classifies samples using hand crafted features which represents information about the samples, weighs the features on how important they are to the final prediction and the resulting computation is compared against a threshold value.

<img width="407" alt="image" src="https://github.com/user-attachments/assets/93430d5f-1af6-4113-b491-f0e7487cf567" />

**X** represents the **inputs** to the model and **W** represents the **weights** (how important are individual features). A linear computation of the weighted sum of features is carried out during the formula below:

<img width="416" alt="image" src="https://github.com/user-attachments/assets/e60b07b1-1cbd-4f94-a757-80ee08418855" />

The value of **z** is then passed through a step function to predict the class of the sample.

<img width="418" alt="image" src="https://github.com/user-attachments/assets/8a8c6712-8182-4060-9612-7079a6bd74a9" />

If **z** is greater than or equal to 0, its predicts one class, else it predicts the other.

At each iteration, the predicted class gets compared to the actual class and the weights gets updated if the prediction was wrong else it is left unchanged in the case of a correct prediction. Updates of weights continue until all samples are correctly predicted, at which point we can say that the perceptron classifier has found a linear decision boundary that perfectly separates all samples into two mutually exclusive classes.

During training the weights are updated by adding a small value to the original weights. The amount added is determined by the perceptron learning rule

<img width="420" alt="image" src="https://github.com/user-attachments/assets/cca65539-afcd-4b14-ae39-374e8b3dad32" />
<img width="408" alt="image" src="https://github.com/user-attachments/assets/cd7382b2-a9ba-427c-9656-92c3c55f8ce9" />

The first coefficient on the right hand side of the equation 2 is called the learning rate and acts as a scaling factor to increase or decrease the extent of the update.

With each pass through the training set, the weights of misclassified examples are nudged in the correct direction so that the value of z can be such that the step function correctly classifies the sample.

Modern iterations are known as **multi-layer** perceptrons. **Multi-layer** perceptrons are feed forward neural networks that have several nodes in the structure of a perceptron. However, there are important differences. A multilayer perceptron is made up of multiple layers of neurons stacked to form a network. The activation functions used are non-linear unlike the perceptron model that uses a step function. The other important difference is that multi-layer perceptrons are trained using a different kind of algorithm called backpropagation which enables training across multiple layers.


### Backpropagation algorithm
It is used to determine how much an input’s features and weights contribute to the final output of the model. Unlike the perceptron learning rule, backpropagation is used to calculate the gradients, which tell us how much a change in the parameters of the model affects the final output. The gradients are used to train the model by using them as an error signal to indicate to the model how far off its predictions are from the ground truth. The backpropagation algorithm can be thought of as the chain rule of derivatives applied across layers.

<img width="423" alt="image" src="https://github.com/user-attachments/assets/c0500843-f2e5-44d1-9560-4a3aab053727" />

The network above is made up of three layers, the input layer which are the features fed into the network, the hidden layer which is so called because we cannot observe what goes on inside and the output layer, through which we get the **prediction** of the model. During training, in order to calculate by how each node contributes to the final prediction and adjust them accordingly to yield a higher accuracy across samples, we need to change the weights using the backpropagation algorithm. It is the weights that are learned during the training process hence they are sometimes referred to as the learnable parameters of the model.

<img width="425" alt="image" src="https://github.com/user-attachments/assets/69005a7e-be9b-4bd4-a106-0d412f933408" />

In the node above x and y are the input features while f is the nonlinear activation function. During training computations are calculated in a forward fashion from the inputs, across the hidden layers, all the way to the output. This is known as the forward pass denoted by green arrows in the image. The prediction of the model is then compared to the ground truth and the error is propagated backwards. This is known as the backward pass and assigns the amount by which every node is responsible for the computed error through the backpropagation algorithm. It is depicted with red arrows in the image above. This process continues until the model finds a set of weights that captures the underlying data representation and correctly predicts majority of samples.
