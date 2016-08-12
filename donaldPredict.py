from sklearn import svm
import numpy as np


def buildX(data2d):
	arrRet = [];
	for row in data2d:
		xRow = row[0:];
		arrRet.append(xRow);
	return arrRet;

def buildY(data2d):
	arrRet = [];
	for row in data2d:
		yRow = row[0];
		arrRet.append(yRow);
	return arrRet;

f = open("donaldtrain.csv")
f1 = open("donaldvalidation.csv")
validationdata=np.loadtxt(f1,delimiter=",")
data=np.loadtxt(f,delimiter=",")

x = buildX(data);
y = validationdata;

clf=svm.SVC();
clf.fit(x,y);

xInput = [ [5466, 763, 589, 32, 54, 32, 362, 335, 50] , [1000, 20, 30, 40, 50, 60, 70, 80, 90] ];
yOutput = clf.predict(xInput);
print(yOutput);

