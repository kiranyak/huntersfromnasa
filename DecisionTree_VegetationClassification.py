""""
 In this context, this work developed an original method to detect in near-real-time the onset of vegetation senescence. The design of the detection relies on the temporal
behavior of two indices: the Normalized Difference Vegetation Index, depending on the
green vegetation, and the Normalized Difference Tillage Index, sensitive to both green
and dry vegetation. The method is demonstrated in Mauritania, an ever-affected country,
with 10-day MODIS mean composites for the years 2010 and 2011. The discrimination
performance of three classes (“growth”, “density reduction” and “drying”) were analyzed for
three classification methods: maximum likelihood (61.4% of overall accuracy), decision tree
(71.5%) and support vector machine (72.3%). The classification accuracy is heterogeneous
in both time and space and is affected by several factors, such as vegetation density, the
north-south climatic gradient and the relief. Smoothing the vegetation time series resulted
in an increase of the overall accuracy of about 5% at the expense of a loss in timeliness of
ten days. To simulate near-real-time monitoring conditions, the decision tree was applied to
the decade of 2010. Overall, the seasonal vegetation cycle appeared clear and consistent.
The results obtained pave the way for an operational implementation of the senescence
dynamic mapping and, consequently, to further strengthen the capacity of the locust
control management.


""""
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
