# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 16:01:00 2018

@author: Mathias
"""

"""
autod erinevate andmetega. 
scikit-learn, pandas packetid.  import sklearn, pole mul olemas
anacondas peaks olemas
esmalt andmed .csv formaatis.
andmed-ettevalmistus-katsed(DT,ANN)
tulemuseks räägi kokkuvõttes raportis tulemusest. See on vaja esitada
atribuutid teisendada numbriteks

"""

import pandas
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_fscore_support
from sklearn import tree
from sklearn import neural_network
#import sklearn
from sklearn.utils import resample
# veergude nimed võetud kirjeldusest
features = ["buying", "maint", "doors", "persons", "lug_boot", "safety"]        
                                                                                
car_data = pandas.read_csv("car.data",                                          
    header=None,  #header näitab kas üks esimene rida on header                                                              
    names=features + ["class"])   # lisab kõik featurid ja seejärel viimane column on class
#1725    low    low  5more    more      big   high  vgood
#print(car_data)
print(car_data)
X_text = car_data.loc[:, features]
#print(X_text)
X = pandas.get_dummies(X_text) # teeb kõik erinevevad safety variablid low/med/highiks ja teeb neist 1 0 dummid                                       
#print(X)
#print(X.columns)                                                                

y = car_data["class"]
#print(y)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3)
# no shuffling
#X_train, X_test, y_train, y_test = train_test_split(
 #   X, y, test_size=0.3, shuffle=False) # võtab kõikidest arraydest 30% ära, teeb test andmeteks
#print(X_train, X_test, y_train, y_test)
dtc=tree.DecisionTreeClassifier()
#print(dtc)
dtc.fit(X_train, y_train)
#print(dtc.fit(X_train, y_train))
# puu on treenitud, vaatame kiirelt, kui hästi ta testandmeid klassifitseerib:
dtc.score(X_test, y_test)
#print(dtc.score(X_test, y_test))
#print
n_features = X_train.shape[1]  # 21 dummit ehk columnit
nnc_shape = (n_features, n_features, 10)
print(nnc_shape)
nnc = neural_network.MLPClassifier(hidden_layer_sizes=nnc_shape, max_iter=1000)
print(nnc)
nnc.fit(X_train, y_train)
nnc.score(X_test, y_test)
#print(nnc)
y_nnc = nnc.predict(X_test)
precision, recall, _, _ = precision_recall_fscore_support(y_nnc, y_test, average=None, labels=["vgood"])
print(precision)
print(nnc.score(X_test, y_test))
#print(_, _)
X1 = X_train[y_train == "unacc"]
X2 = X_train[y_train == "acc"]
X3 = X_train[y_train == "good"]
X4 = X_train[y_train == "vgood"]
y1 = y_train[y_train == "unacc"]
y2 = y_train[y_train == "acc"]
y3 = y_train[y_train == "good"]
y4 = y_train[y_train == "vgood"]
#print(y4)

biggest_class = X1.shape[0]

X2r, y2r = resample(X2, y2, n_samples=biggest_class)
X3r, y3r = resample(X3, y3, n_samples=biggest_class)
X4r, y4r = resample(X4, y4, n_samples=biggest_class)


#print(X4r.shape)

X_balanced = pandas.concat([X1, X2r, X3r, X4r])
y_balanced = pandas.concat([y1, y2r, y3r, y4r])
#print(X_balanced)
precision, recall, _, _ = precision_recall_fscore_support(y_nnc, y_test, average=None, labels=["vgood"])
newDataSet=neural_network.MLPClassifier(hidden_layer_sizes=nnc_shape, max_iter=1000)
Xbalanced_train, Xbalanced_test, ybalanced_train, ybalanced_test = train_test_split(
    X_balanced, y_balanced, test_size=0.3)
newDataSet.fit(Xbalanced_train, ybalanced_train)
newDataSet.score(Xbalanced_test, ybalanced_test)

print(newDataSet.score(Xbalanced_test, ybalanced_test))#print(precision)
ybalanced_nnc = newDataSet.predict(Xbalanced_test)
precisionbalanced, recallbalanced, _, _ = precision_recall_fscore_support(ybalanced_nnc, ybalanced_test, average=None, labels=["vgood"])
print(precisionbalanced)
#print(nnc.score(X_test, y_test))
#nnc = neural_network.MLPClassifier(hidden_layer_sizes=(1,), max_iter=1000)
#nnc.fit(X_train, y_train)
#nnc.score(X_test, y_test)
#print(nnc.score(X_test, y_test))