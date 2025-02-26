import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# 1. Load the dataset
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

plt.imshow(np.reshape(x_train[2], (28, 28)))
plt.show()

# Normalize the data
x_train, x_test = x_train / 255.0, x_test / 255.0

# Convert labels to one-hot encoding
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

# 2. Define the model with default weights and biases
# The default weights and learning rate are often set automatically by the framework
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),  # Input layer
    # 128 is a common choice in many neural network architectures. It is a power of 2, which can be beneficial for computational efficiency
    # ReLU (Rectified Linear Unit) introduces non-linearity into the model
    tf.keras.layers.Dense(128, activation='relu'),  # Hidden layer 1
    # This reduction in size helps the model to progressively distill the most important features extracted by the first layer
    tf.keras.layers.Dense(64, activation='relu'),   # Hidden layer 2
    # Converts raw output scores (logits) into a probability distribution, suitable for multiclass classification and compatible with categorical cross-entropy loss.
    tf.keras.layers.Dense(10, activation='softmax') # Output layer
])

# 3. Loss and optimization
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 4. Batch the model for training
batch_size = 32
epochs = 5

# Create a TensorFlow Dataset
train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
train_dataset = train_dataset.shuffle(buffer_size=1024).batch(batch_size).prefetch(tf.data.AUTOTUNE)

# Train the model
model.fit(train_dataset, epochs=epochs)

# 5. Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f'\nTest accuracy: {test_acc:.4f}')