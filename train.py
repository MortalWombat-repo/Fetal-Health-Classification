#!/usr/bin/env python
# coding: utf-8

import pickle

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
#from sklearn.model_selection import KFold

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score


# parameters
output_file = 'model.bin'

# data preparation
df = pd.read_csv("transformed_fetal_health.csv")

# spliting with scikit learn
df_full_train, df_test = train_test_split(df, test_size=0.2, stratify=df['fetal_health'], random_state=1)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, stratify=df_full_train['fetal_health'], random_state=1)

#resetting index
df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

#extracting the target values
y_train = df_train.fetal_health.values
y_val = df_val.fetal_health.values
y_test = df_test.fetal_health.values

#deleting the targets from training data
del df_train['fetal_health']
del df_val['fetal_health']
del df_test['fetal_health']

X_train = df_train
X_val = df_val
X_test = df_test

# spliting into categories not needed, all data is numerical

print("Unique values in fetal_health:", df['fetal_health'].unique())
'''
# training
def train(X_train, y_train):
    model = DecisionTreeClassifier( class_weight='balanced', 
                                    max_depth=6, 
                                    min_samples_leaf=10, 
                                    random_state=1
                                    )                            
    model.fit(X_train, y_train)
    return model

model = train(X_train, y_train)

# training the final model
print('training the final model')

# Save the model
with open(output_file, 'wb') as f_out:
    pickle.dump(model, f_out)

print(f'the model is saved to {output_file}')
'''
