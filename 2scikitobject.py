import subprocess 
import re
from sklearn import svm
import numpy as np
import os
import sys
import operator # map(operator.add, first,second) to add 2 arrays 
import math
#from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn import neighbors, datasets

# or use np.add(first,second) 
#####################################################################################

class Aiobject:

	def __init__(self, training, validation, results):
		self.train = training
		self.valid = validation
 		self.daily = []
		self.result= results
		self.temp2 = "/home/admin/Downloads/temp2.csv"	
####################################################################################

	def buildX(self, array):
		arrRet = [];
		for row in array:
			xRow = row[0:];
			arrRet.append(xRow);
		return arrRet;

####################################################################################

	def getdata(self):
		
		dates = []
		data  = []	
		outfile = open(self.temp2, "w")
		ax = 0
		with open(self.train) as infile:
			for line in infile:
				line = line.rstrip('\n')
				data.append(line[12:-6])	# makes a list of lists from file
				dates.append(line[:11])
				outfile.write(str(data[ax]))
				outfile.write('\n')
				ax+=1
			print(data)
			outfile.close()
							
					
	#	print(data
		twodarray = [[] for x in range(len(data))]			# initialize arrays 
		avgarray = [[] for x in range(len(data)/24)]
		
		for i in range(len(data)):					# for length of data 
			data2 = data[i]
			data2 = data2.split(",")					# gets rid of commas to be treated as an arary
			for j in range(len(data2)):				
				data2[j]= float(int(data2[j]))				# converts strings to ints
			data2 = np.asarray(data2)				# converts each list into an array 
			twodarray[i] = data2					# makes an array of array [ [...] , [....], [...] ] 
			
		
		self.daily = [[0,0,0,0,0,0,0,0,0] for i in range(len(twodarray)/24)]   # Initialize daily array
		for c in range(8): 							# to cycle through columns
			results = []
			for a in range(len(twodarray)):					# makes 1d array of a single column of results data
				results.append(twodarray[a][c])				
				
			for b in range(int(math.ceil(float(len(results)/24)))): 	# is /24 since we only need 1/24 as many spaces to store the data
				try:
					self.daily[b][c] = int(math.ceil(float(sum(results[b*24:(b*24+23)]))/24))	# gets average of 24 lines of training data at a time
				except IndexError:						# just in case
					print("end of days")	
#		print(self.daily)
		output = ''
		outfile = open("/home/admin/Downloads/temp.csv", "w+")
		for i in range (len(self.daily)):		# writes to csv file so it can be read
			print(str(self.daily[i]))		# with np loads. 
			output =  str(self.daily[i]).rstrip(']')
			output = output.lstrip('[')  
			outfile.write(output)
			outfile.write('\n')
		outfile.close()
		return(dates)
#		starttraining(self, x , y)

##################################################################################


	def starttraining(self, a, b, case_id, d):
		# clf=svm.SVC();
		#clf = NearestCentroid();
		clf = neighbors.KNeighborsClassifier(1, 'distance'); 
		clf.fit(a,b); 			# fit for daily
						# take in file input average on a 
		print("------------- X axis -----------------\n");
#		for val in a:
#			for ele in val:
#				print ele,
#			print("");
		print("------------- Y axis -----------------\n");
		print(b);
		print("------------- xInput -----------------\n");
		xInput = np.loadtxt(open("/home/admin/Downloads/temp.csv"), delimiter = ",")
#		for val in xInput:
#			for ele in val:
#				print ele,
#			print("");
		yOutput = clf.predict(xInput); # predict for hourly
		print("\n------------- PREDICTION BELOW -----------------\n");
		outfile3 = open(self.result,"a+")
		cnt = 0;
		dx = 0
		print("---------------------------------Dcount is----------------")
		print(d)
		for val in yOutput:
	#		print(d[cnt]+ str(val)+case_id)
			cnt = cnt + 1;
			outfile3.write(d[cnt*23]+str(int(val))+","+case_id+"\n")
			dx+=1
			if cnt ==23:
				cnt = 0;
			
				
		print("------------- PREDICTION per 24 hours BELOW -----------------\n");
		cnt = 0;
		sum = 0.0;
		ax=0
		outfile2 = open(self.result,"a+")
		for val in yOutput:
			sum = sum + val;
			cnt = cnt + 1;
			if(cnt==23):
			#	outfile2.write((d[cnt*ax]+str(int(sum*1.0/cnt))+ ","+case_id+"\n"));
				cnt = 0;
				sum = 0.0;
				ax+=1
		outfile2.close()
		
##################################################################################

# trump = Aiobject("/home/admin/Downloads/donald1training.txt" , "/home/admin/Downloads/donaldvalidation.csv")
caseID = sys.argv[1]
#trainfile = sys.argv[2]
name = caseID
predictionfile = "/home/admin/Downloads/UserA/personprediction.csv"
caseID = Aiobject("/home/admin/Downloads/UserA/persontraining.txt" , "/home/admin/Downloads/cruzvalidation.csv", predictionfile)
dates1 = caseID.getdata()
z = np.loadtxt(open("/home/admin/Downloads/temp.csv"), delimiter = ",")
x = caseID.buildX(z)
y = np.loadtxt(open(caseID.valid),delimiter=",") # validation data 
deletefile ="rm /home/admin/Downloads/temp.csv"
#subprocess.call(deletefile, shell = True)
caseID.starttraining(x, y, name,dates1)
