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

LR=LogisticRegression(solver='liblinear',multi_class='ovr')
LDA=LinearDiscriminantAnalysis()
KNN=KNeighborsClassifier()
CART=DecisionTreeClassifier()
NB=GaussianNB()
SVM=SVC(gamma='auto')


'''
traindata['ltiFeatures']=traindata['ltiFeatures'].apply(ast.literal_eval)
traindata['stiFeatures']=traindata['stiFeatures'].apply(ast.literal_eval)
valdata['ltiFeatures']=valdata['ltiFeatures'].apply(ast.literal_eval)
valdata['stiFeatures']=valdata['stiFeatures'].apply(ast.literal_eval)
'''
''' Till this much needs to remain as it is, feel free to change remaining'''


#print(infodata.head(20))


#The following code breaks down interests as per depth level.

x={1:[],2:[],3:[],4:[],5:[],6:[]}
y={}
w={1:[],2:[],3:[],4:[],5:[],6:[]}
v={}
u={}
for index, row in infodata.iterrows():
    string=row['topic_name']
    id=row['topic_id']
    depth=string.count('/')
    x[depth].append(id)
    w[depth].append(string)
    y[id]=depth
    v[string]=depth
    u[string]=id


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

#The following code shows that the avg depth of long term interests does not influence conversion
'''
meanweighttrue=0
meanweightfalse=0
for index, row in traindata.iterrows():
    lti=row['ltiFeatures']
    lti=ast.literal_eval(lti)
    ltikeys=lti.keys()
    weightltikeys=0
    for i in ltikeys:
        j=int(i)
        if (j in y.keys()):
            weightltikeys=weightltikeys+ (y[j]/6)*lti[i]
    k=row['userID']
    if (k<1500):
        meanweighttrue=meanweighttrue+weightltikeys
    else:
        meanweightfalse=meanweightfalse+weightltikeys
meanweighttrue=meanweighttrue/1465
meanweightfalse=meanweightfalse/94941
print (meanweighttrue)
print (meanweightfalse)
'''



#Same as previous, but for short term interests
'''
meanweighttrue=0
meanweightfalse=0
for index, row in traindata.iterrows():
    lti=row['stiFeatures']
    lti=ast.literal_eval(lti)
    ltikeys=lti.keys()
    weightltikeys=0
    for i in ltikeys:
        j=int(i)
        if (j in y.keys()):
            weightltikeys=weightltikeys+ (y[j]/6)*lti[i]
    k=row['userID']
    if (k<1500):
        meanweighttrue=meanweighttrue+weightltikeys
    else:
        meanweightfalse=meanweightfalse+weightltikeys
meanweighttrue=meanweighttrue/1465
meanweightfalse=meanweightfalse/94941
print (meanweighttrue)
print (meanweightfalse)
'''
z={}
for i in w[1]:
    z[i]=i
for index, row in infodata.iterrows():
    string=row['topic_name']
    if (string not in z.keys()):
        sh=string[1:]
        ind=sh.find('/')
        st=string[0:ind+1]
        z[string]=st

    
qtr={}
for i in z.keys():
    qtr[u[i]]=u[z[i]]

print (qtr)



