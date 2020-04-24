"""
    Image Classification
    COVID19 Chest XRay Data-Set

    TensorFlow :)

"""

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

print(">> IMAGE CLASSIFICATION MODEL CREATION")

print()

print(">> STEP#1 IMAGE PRE-PROCESSING")
train_image_generator = ImageDataGenerator(rescale=1.0/255)
test_image_generator = ImageDataGenerator(rescale=1.0/255)

training_images = train_image_generator.flow_from_directory(
                                        'covid19dataset/train',
                                        target_size=(64, 64),
                                        batch_size=8,
                                        class_mode='binary')

testing_images = test_image_generator.flow_from_directory(
                                        'covid19dataset/test',
                                        target_size=(64, 64),
                                        batch_size=8,
                                        class_mode='binary')
def plotImages(images):
    fig, axes = plt.subplots(1, 5, figsize=(20, 20))
    axes = axes.flatten()
    for img, ax in zip(images, axes):
        ax.imshow(img)
        ax.axis('off')
    plt.tight_layout()
    plt.show()

sample_training_images, _ = next(training_images)
# plotImages(sample_training_images[:5])


print(">> STEP#2 CREATE CNN MODEL")
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))

# Further Adding the NeuralNet in ConvNet Model
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

print(">> STEP#3 TRAIN THE MODEL")
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# use fit_generator instead of fit  -> if we have used ImageDataGenerator for our Image Data Set Creation
history = model.fit_generator(training_images, epochs=5, validation_data=testing_images)

print(">> STEP#4 VISUALIZING ACCURACY AND LOSS")
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(5)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('ACCURACY')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper left')
plt.title('LOSS')

plt.show()

"""
After the observations on our training and testing images, 
we might would not have found the correct modeling for our data set

1. Either, we gather more images and more meaningful images and work again to train the model
2. Perform Image Augmentation
    From the  training images and testing images we gonna create more set where we flip the images, rotate the images etc
    For Image Augmentation -> https://www.tensorflow.org/tutorials/images/classification

HW: -> Predict the class from the Given Image to the MODEL :)

"""