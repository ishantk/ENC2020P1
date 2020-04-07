# TensorFlow Installation Link
# https://www.tensorflow.org/install

# Requires the latest pip
# pip install --upgrade pip

# Current stable release for CPU and GPU
# pip install tensorflow

# Link to Tutorials:
# https://www.tensorflow.org/tutorials

import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

print(tf.__version__)


hello = tf.constant("Hello from Tensorflow")
print(hello)