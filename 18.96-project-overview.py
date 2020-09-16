import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler


#K Nearest Neighbors Project
#Get the Data
#** Read the 'KNN_Project_Data csv file into a dataframe **
df = pd.read_csv(r'.\udemy\python-for-data-science-and-machine-learning-bootcamp\18\KNN_Project_Data.csv')
#Check the head of the dataframe.
print("df.head():")
print(df.head())
print("**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--")

#Since this data is artificial, we'll just do a large pairplot with seaborn.
#Use seaborn on the dataframe to create a pairplot with the hue indicated by the TARGET CLASS column.
#sns.pairplot(df, hue='TARGET CLASS', palette='coolwarm')
#plt.show()

#Standardize the Variables
#Time to standardize the variables.
#** Import StandardScaler from Scikit learn.**
#** Create a StandardScaler() object called scaler.**
scaler = StandardScaler()
#** Fit scaler to the features.**
scaler.fit(df.drop('TARGET CLASS', axis=1))
#Use the .transform() method to transform the features to a scaled version.
scaled_features = scaler.transform(df.drop('TARGET CLASS', axis=1))
#Convert the scaled features to a dataframe and check the head of this dataframe
# to make sure the scaling worked.
df_feat = pd.DataFrame(scaled_features, columns=df.columns[:-1])
print("df_feat.head():")
print(df_feat.head())
print("**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--")

#Train Test Split
#Use train_test_split to split your data into a training set and a testing set.
X = df_feat
y = df['TARGET CLASS']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=101)

#Using KNN
#Import KNeighborsClassifier from scikit learn.
#Create a KNN model instance with n_neighbors=1
knn = KNeighborsClassifier(n_neighbors=1)
#Fit this KNN model to the training data.
knn.fit(X_train, y_train)

#Predictions and Evaluations
#Let's evaluate our KNN model!
#Use the predict method to predict values using your KNN model and X_test.
pred = knn.predict(X_test)
#** Create a confusion matrix and classification report.**
print(f"confusion_matrix: {confusion_matrix(y_test, pred)}")
print("**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--")

print(f"classification_report: {classification_report(y_test, pred)}")
print("**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--")


#Let's go ahead and use the elbow method to pick a good K Value!
#** Create a for loop that trains various KNN models with different k values,
# then keep track of the error_rate for each of these models with a list.
# Refer to the lecture if you are confused on this step.**
error_rate = []

for i in range(1,40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))

#Now create the following plot using the information from your for loop.
plt.figure(figsize=(10,6))
plt.plot(range(1, 40), error_rate, color='blue', linestyle='dashed', marker='o', markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')
plt.show()

#Retrain with new K Value
#Retrain your model with the best K value (up to you to decide what you want) and re-do the classification report and the confusion matrix.
knn = KNeighborsClassifier(n_neighbors=30)
knn.fit(X_train, y_train)
pred = knn.predict(X_test)
print(f"confusion_matrix: {confusion_matrix(y_test, pred)}")
print("**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--")

print(f"classification_report: {classification_report(y_test, pred)}")
print("**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--**--")
