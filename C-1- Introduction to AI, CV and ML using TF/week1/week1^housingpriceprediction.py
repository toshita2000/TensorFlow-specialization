#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf
import numpy as np
from tensorflow import keras


# In[2]:


def house_model(y_new):
 model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
 model.compile(optimizer='sgd',  loss='mean_squared_error')
 xs = np.array([1, 2, 3, 4])
 ys = np.array([100, 150, 200, 250]) / 100
 model.fit(xs, ys, epochs=1000)
 return model.predict(y_new)[0]


# In[3]:


prediction = house_model([7.0])
print(prediction)


# In[ ]:




