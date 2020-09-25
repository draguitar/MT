# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 14:52:39 2020

@author: C09700
"""
# %%
import pandas as pd
from tensorflow.keras.callbacks import TensorBoard
from kashgari.tasks.classification import CNN_Model
from sklearn.model_selection import train_test_split

# %%
with open('dataset/X-jieba.csv', encoding='utf-8') as f:
    text = []
    for line in f:
        text.append(line.strip())
print(text)
# %%
# Using TensorBoard record training process
tf_board = TensorBoard(log_dir='tf_dir/cnn_model',
                       histogram_freq=5, 
                       update_freq='batch')

model = CNN_Model()
model.fit(train_x, train_y, val_x, val_y,
          batch_size=128,
          callbacks=[tf_board])
# %%
print(type(test_data))
# %%%