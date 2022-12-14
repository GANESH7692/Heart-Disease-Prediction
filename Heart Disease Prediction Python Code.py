#importing dependencies

#numpy is used to run the numerical operations
import numpy as np
#for data visualization with use pandas
import pandas as pd
#to train and test the model we use train_test_split from the library sklearn
from sklearn.model_selection import train_test_split
# we are going to use logisticregression algorithm in this project so, to use logisticregression algo directly we use this command 
from sklearn.linear_model import LogisticRegression
#this command is used to evaluate our model
from sklearn.metrics import accuracy_score

# loading the csv data to a Pandas DataFrame
df = pd.read_csv('/content/heart.csv')

#to print first 5 rows of the dataframe we use head function
df.head()

#to know the rows and columms in a dataframe we use the command shape
df.shape

# defective heart is represented by 1
# healthy heart is represented by 0
# checking that how many patients having the defective heart and how many having the healthy heart
df['target'].value_counts()

"""**As we can see 165 patients having a defective heart and 138 patients having a healthy heart**"""

# Spliting the features and target in the dataframe
X = df.drop(columns='target', axis=1)
Y = df['target']

#checking whether the command worked properly or not
print(X)

print(Y)

"""**Spliting the data into Training Data and testing data**"""

# test_size is the number that defines the size of the test set
# stratify parameter makes a split so that the proportion of values in the sample produced will be the same as the proportion of values provided to parameter stratify.
# which will decide the splitting of data into train and test...we can only two states 1 and 0
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""### **Model Training**"""

# for this type of models LogisticRegression algo will be the best option
lr = LogisticRegression()

# training the LogisticRegression model with Training data
lr.fit(X_train, Y_train)

"""### **Model Evaluation**"""

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()

# accuracy on training data
X_train_prediction = lr.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy on Training data = ', (float(training_data_accuracy)) * 100,'%')

"""### **Buliding The Prediction System**"""

input_data = (62,0,0,140,268,0,0,160,0,3.6,0,2,2)

# change the input data to a numpy array
input_data_as_numpy_array= np.asarray(input_data)

# reshape the numpy array as we are predicting for only on instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = lr.predict(input_data_reshaped)
print(prediction)

if (prediction[0]== 0):
  print('The patient is not suffering from any heart disease')
else:
  print('The patient is suffering from a heart disease')

input_data = (56,1,1,120,236,0,1,178,0,0.8,2,0,2)

# change the input data to a numpy array
input_data_as_numpy_array= np.asarray(input_data)

# reshape the numpy array as we are predicting for only on instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = lr.predict(input_data_reshaped)
print(prediction)

if (prediction[0]== 0):
  print('The patient is not suffering from any heart disease')
else:
  print('The patient is suffering from a heart disease')
