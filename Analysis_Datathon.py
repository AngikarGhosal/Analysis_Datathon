# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 10:14:07 2019

@author: angik
"""
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

infofile = "interest_topics.csv"
trainfile = "training.csv"
valfile = "validation.csv"
infodata = pandas.read_csv(infofile)
traindata = pandas.read_csv(trainfile)
valdata = pandas.read_csv(valfile)
print(infodata.head(20))