"""

    CNN Tutorial From Tensorflow:
    https://www.tensorflow.org/tutorials/images/cnn

    ML Glossary: https://developers.google.com/machine-learning/glossary/#c

"""

import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

# This data set will be downloaded first if not available in the system
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()

# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

print("==IMAGES==")
print(train_images[0])

print("==LABELS==")
print(train_labels[0])

# We got 10 classes in the data set
# 0 to 9
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

"""
plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    # The CIFAR labels happen to be arrays,
    # which is why you need the extra index
    plt.xlabel(class_names[train_labels[i][0]])
plt.show()
"""

# In Conv Net -> We put number of filters in the power of 2 and as layers increase we increase filters

# Creation of ConvNet Model
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

# Further Adding the NeuralNet in ConvNet Model
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10)) # Final Output Layer with 10 results :)

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

history = model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))

test_loss, test_acc = model.evaluate(test_images,  test_labels)
print(">> TEST ACCURACY:", test_acc)

# HW: 1. Explore Cats and Dogs Image Classification Problem: https://www.tensorflow.org/tutorials/images/classification
#     2. Hand Written Image Data Set :)