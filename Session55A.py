"""
    What is a Tensor ?
    Tensor is n-Dimensional Array
"""

import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

"""
A = tf.constant([[1.0, 2.0], [3.0, 4.0]])
B = tf.constant([[1.0, 1.0], [0.0, 1.0]])

print(A)
print(B)

C = tf.matmul(A, B)
print(C)
"""

A = tf.constant([1, 2, 3, 4, 5])
B = tf.constant([6, 7, 8, 9, 10])

C = tf.multiply(A, B)
print(C)



# Previously we would have to create Sessions to solve these kind of problems,
# But now its done automatically -> EAGER EXECUTIONS

# OLD Approaches with Session
# Kind of Deprecated

# session = tf.compat.v1.Session()
# print(session.run(C))
# session.close()

# with tf.compat.v1.Session() as session:
#     output = session.run(C)
#     print(output)
