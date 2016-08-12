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

	def __init__(self, training, validation):
		self.train = training
		self.valid = validation
 		self.daily = []	
####################################################################################

	def buildX(self, array):
		arrRet = [];
		for row in array:
			xRow = row[0:];
			arrRet.append(xRow);
		return arrRet;

####################################################################################

	def getdata(self):
		

		data=[]		
		with open(self.train) as infile:
			for line in infile:
				line = line.rstrip('\n')
	#			print(line)
				data.append(line)				# makes a list of lists from file
	#	print(data
		twodarray = [[] for x in range(len(data))]			# initialize arrays 
		avgarray = [[] for x in range(len(data)/24)]
		
		for i in range(len(data)):					# for length of data 
			data2 = data[i]
			data2=data2.split(",")					# gets rid of commas to be treated as an arary
			for j in range(len(data2)):				
				data2[j]= float(data2[j])				# converts strings to ints
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
			output=  str(self.daily[i]).rstrip(']')
			output = output.lstrip('[')  
			outfile.write(output)
			outfile.write('\n')
		outfile.close()
		
#		starttraining(self, x , y)

##################################################################################

	def insertPredictionRecord(case_id, value, timestamp):
		print("Unimpemented yet!!! insertPredictionRecord insert id: ");

	def starttraining(self, a, b, case_id):
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
		xInput = np.loadtxt(open(self.train), delimiter = ",")
#		for val in xInput:
#			for ele in val:
#				print ele,
#			print("");
		yOutput = clf.predict(xInput); # predict for hourly
		print("\n------------- PREDICTION BELOW -----------------\n");
		cnt = 0;
		for val in yOutput:
			print val, 
			cnt = cnt + 1;
			if cnt ==23:
				cnt = 0;
				print "\n";
				
		print("------------- PREDICTION per 24 hours BELOW -----------------\n");
		cnt = 0;
		sum = 0.0;
		for val in yOutput:
			sum = sum + val;
			cnt = cnt + 1;
			if(cnt==23):
				print(sum*1.0/cnt);
				cnt = 0;
				sum = 0.0;
#
##################################################################################

# trump = Aiobject("/home/admin/Downloads/donald1training.txt" , "/home/admin/Downloads/donaldvalidation.csv")
case_id = 4;
caseID = sys.argv[1]
trainfile = sys.argv[2]

trump = Aiobject("/home/admin/Downloads/cruz1training.txt" , "/home/admin/Downloads/cruzvalidation.csv")
trump.getdata()
z = np.loadtxt(open("/home/admin/Downloads/temp.csv"), delimiter = ",")
x = trump.buildX(z)
y = np.loadtxt(open(trump.valid),delimiter=",") # validation data 
deletefile ="rm /home/admin/Downloads/temp.csv"
#subprocess.call(deletefile, shell = True)
trump.starttraining(x, y)
