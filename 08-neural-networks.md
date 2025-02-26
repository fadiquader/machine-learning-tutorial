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



## Simplified explaination 
Sure! Let's break down the Perceptron algorithm and how it works with neural networks, including input features, activation functions, and backpropagation, in a simple way.

### The Perceptron Algorithm

Imagine you have a simple machine that can decide whether to let you into a special club based on two things: your height and your age. The Perceptron algorithm is like a simple decision-making machine that uses these two inputs to make a choice.

#### Input Features
- **Height**: This is one feature.
- **Age**: This is another feature.

These features are like the information the machine uses to make its decision.

#### Weights and Bias
- **Weights**: These are like the importance given to each feature. For example, the machine might care more about your age than your height.
- **Bias**: This is like a starting point or a threshold that helps the machine make its decision.

#### Activation Function
The activation function is like a rule that the machine uses to decide whether to let you in or not. A simple example is the "step function":
- If the weighted sum of your height and age is greater than a certain threshold (bias), you get in.
- Otherwise, you don't.

### Example
Let's say:
- Height (H) = 6 feet
- Age (A) = 25 years
- Weight for height (W1) = 2
- Weight for age (W2) = 3
- Bias (B) = 50

The machine calculates:

<img width="622" alt="image" src="https://github.com/user-attachments/assets/45add7d8-e2f4-4b44-b111-72fa60614d24" />


If the weighted sum is greater than a certain threshold (let's say 100), you get in. In this case, 137 is greater than 100, so you get in!

### Neural Networks and Backpropagation

Now, let's make this a bit more complex with a neural network. Imagine the club has multiple bouncers (layers) who each make a decision based on different features.

#### Multi-Layer Neural Network
- **Input Layer**: This is where the height and age go in.
- **Hidden Layers**: These are like intermediate bouncers who make decisions based on the inputs.
- **Output Layer**: This is the final decision.

#### Weights and Bias in Hidden Layers
Each connection between layers has a weight, and each neuron (bouncer) has a bias. These help the network make more complex decisions.

#### Activation Function in Hidden Layers
Each neuron uses an activation function to decide whether to pass the signal forward. A common one is the "ReLU" function, which is like saying:
- If the input is positive, pass it forward.
- If the input is negative, don't pass it forward.

### Backpropagation
Backpropagation is like the club owner telling the bouncers how to improve their decisions based on past mistakes.

1. **Forward Pass**: The network makes a decision based on the current weights and biases.
2. **Calculate Error**: The network sees if its decision was right or wrong.
3. **Backward Pass**: The network adjusts the weights and biases to reduce the error. This is done using a method called gradient descent, which is like finding the steepest path down a hill to reach the lowest point (the least error).

### Example with Backpropagation
Let's say the network initially made a wrong decision. It thought you should be let in, but you shouldn't have been. Here's what happens:
1. **Forward Pass**: The network calculates the weighted sum and applies the activation function.
2. **Calculate Error**: The network sees the mistake.
3. **Backward Pass**: The network adjusts the weights and biases slightly to reduce the error. For example, it might reduce the weight for height and increase the weight for age.

### Summary
- **Input Features**: These are the information the network uses (like height and age).
- **Weights and Bias**: These help the network make decisions.
- **Activation Function**: This is the rule the network uses to decide what to do with the information.
- **Backpropagation**: This is how the network learns from its mistakes and adjusts its weights and biases to make better decisions.

By repeating this process many times with different examples, the network gets better at making the right decisions!

Sure! Let's dive deeper into a multi-layer neural network (MLN) and see how it works with hidden layers and how the weights change in each layer using backpropagation. We'll use a simple example to make it easy to understand.

### More on Multi-Layer Neural Network (MLN)

### Example

Let's use the same example of deciding whether to let someone into a club based on height and age. But this time, we'll add a hidden layer to make the decision process more complex.

#### Input Layer
- **Height (H)**: 6 feet
- **Age (A)**: 25 years

#### Hidden Layer 1
- **Neuron 1**: Uses height and age to make a decision.
- **Neuron 2**: Also uses height and age but might weigh them differently.

#### Output Layer
- **Final Decision**: Based on the outputs from the hidden layer.

### Weights and Biases
Each connection between neurons has a weight, and each neuron has a bias. These are the parameters that the network will adjust to learn.

### Activation Function
Each neuron uses an activation function. Let's use the ReLU function for simplicity:
- If the input is positive, pass it forward.
- If the input is negative, don't pass it forward.

### Example with Hidden Layers

#### Step 1: Forward Pass

1. **Input Layer**:
   - Height (H) = 6 feet
   - Age (A) = 25 years

2. **Hidden Layer 1**:
   - Neuron 1:
     - Weight for height (W1) = 2
     - Weight for age (W2) = 3
     - Bias (B1) = 5
     - Calculation: Weighted Sum = (6 * 2) + (25 * 3) + 5 = 12 + 75 + 5 = 92
     - Activation: ReLU(92) = 92 (since 92 is positive)
   - Neuron 2:
     - Weight for height (W3) = 1
     - Weight for age (W4) = 4
     - Bias (B2) = 10
     - Calculation: Weighted Sum = (6b* 1) + (25 * 4) + 10 = 6 + 100 + 10 = 116
     - Activation: ReLU(116) = 116 (since 116 is positive)

3. **Output Layer**:
   - Weight for Neuron 1 output (W5) = 0.5
   - Weight for Neuron 2 output (W6) = 0.3
   - Bias (B3) = 20
   - Calculation: Weighted Sum = (92 * 0.5) + (116 * 0.3) + 20 = 46 + 34.8 + 20 = 100.8 
   - Activation: ReLU(100.8) = 100.8 (since 100.8 is positive)

The final decision is based on the output of the output layer. If the threshold is 100, then 100.8 means you get in.

### Step 2: Backpropagation

Now, let's say the network made a mistake. It let you in, but you shouldn't have been let in. Here's how it adjusts:

1. **Calculate Error**: The network sees the mistake. Let's say the error is the difference between the actual output (100.8) and the correct output (let's say it should have been 90 to not let you in).

2. **Backward Pass**:
   - **Output Layer**:
     - Adjust weights and bias to reduce the error. For simplicity, let's say we reduce W5 and W6 slightly and adjust B3.
   - **Hidden Layer 1**:
     - Adjust weights and biases in the hidden layer based on the changes in the output layer. For example, reduce W1, W2, W3, and W4 slightly and adjust B1 and B2.

### Example of Weight Adjustment

Let's say we reduce the weights by a small amount (let's say 0.1 for simplicity):

1. **Output Layer**:
   - New W5 = 0.5 - 0.1 = 0.4
   - New W6 = 0.3 - 0.1 = 0.2
   - New B3 = 20 - 0.1 = 19.9

2. **Hidden Layer 1**:
   - New W1 = 2 - 0.1 = 1.9
   - New W2 = 3 - 0.1 = 2.9
   - New W3 = 1 - 0.1 = 0.9
   - New W4 = 4 - 0.1 = 3.9
   - New B1 = 5 - 0.1 = 4.9
   - New B2 = 10 - 0.1 = 9.9
  
sts the weights and biases in each layer to reduce the error and improve the decision-making process.

