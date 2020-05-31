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

from __future__ import division, print_function
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
import sys
import os

# Import helper functions
from mlfromscratch.utils import train_test_split, standardize, accuracy_score
from mlfromscratch.utils import mean_squared_error, calculate_variance, Plot
from mlfromscratch.supervised_learning import ClassificationTree

def main():

    print ("-- Classification Tree --")

    data = datasets.load_iris()
    X = data.data
    y = data.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)

    clf = ClassificationTree()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    print ("Accuracy:", accuracy)

    Plot().plot_in_2d(X_test, y_pred, 
        title="Decision Tree", 
        accuracy=accuracy, 
        legend_labels=data.target_names)


if __name__ == "__main__":
    main()
