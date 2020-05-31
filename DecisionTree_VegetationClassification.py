
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics 



column_name = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']

dataset = pd.read_csv("diabetes.csv", header=None, names=column_name)

print("top 5 record in dataset is :::::",dataset.head())

featureColumn = ['pregnant', 'insulin', 'bmi', 'age','glucose','bp','pedigree']
X_data = dataset[featureColumn] # Features
y_data = dataset.label # Target variable


X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.25, random_state=1)



obj = DecisionTreeClassifier()

# Train Decision Tree Classifer
obj = obj.fit(X_train,y_train)

#Predict the response for test dataset
y_predicted_data = obj.predict(X_test)
print(type(y_predicted_data))

print("=============y_predicted value:::",y_predicted_data)


# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_predicted_data))

# converting predicted numpy value into dataframe
convert_toDF= pd.DataFrame(y_predicted_data)
print("convert to Dataframe::::::",convert_toDF)


# export output into a csv file
export_csv=convert_toDF.to_csv("X_test.csv",index=False,header=['PredictedValue'])
print("data exported successfully:::",export_csv)
