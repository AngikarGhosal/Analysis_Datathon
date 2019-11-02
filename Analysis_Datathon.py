# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 10:14:07 2019

@author: angik
"""
import pandas
import ast
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
'''
traindata['ltiFeatures']=traindata['ltiFeatures'].apply(ast.literal_eval)
traindata['stiFeatures']=traindata['stiFeatures'].apply(ast.literal_eval)
valdata['ltiFeatures']=valdata['ltiFeatures'].apply(ast.literal_eval)
valdata['stiFeatures']=valdata['stiFeatures'].apply(ast.literal_eval)
'''
''' Till this much needs to remain as it is, feel free to change remaining'''


#print(infodata.head(20))


#The following code breaks down interests as per depth level.
'''
x={1:[],2:[],3:[],4:[],5:[],6:[]}
for index, row in infodata.iterrows():
    string=row['topic_name']
    depth=string.count('/')
    x[depth].append(string)

print (x[1])
print ('These are the broad topics')
'''


#The following code shows that you are more likely to not have short term interests, if you are a convert.
'''

nostifalse=0
nostitrue=0
for index, row in traindata.iterrows():
    dic=row['stiFeatures']
    k=row['userID']
    if (len(dic)==2):
        if (k<1500):
            nostitrue=nostitrue+1
        else:
            nostifalse=nostifalse+1
            
print (nostitrue, " out of 1465 ", nostitrue/1465)
print (nostifalse, " out of 94941", nostifalse/94941)

'''