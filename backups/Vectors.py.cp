import sys
import time
import optparse
import os
import string 
import re
import subprocess

class VectorModel:  				
	def __init__(self, file):  
		self.querylist = []   
		self.queryfile= file	
		self.vectorlist= []
		
###################################################################################						
		
		
	def populatelist(self): #DONE!!!!!!!!!!!!!!!
		with open(self.queryfile) as input:
			#for line in open(filename)
				self.querylist = [line.rstrip('\n') for line in open(self.queryfile)] 
	

###################################################################################		

 		
	def createlist(self, Parsedfile): 
		deletetemp = "rm tempfile.txt"  
		for i in range (len(self.querylist)):
			
			output =('match -f ' + Parsedfile + ' -t '+ str(self.querylist[i]) + '>> tempfile.txt')
			#"(echo stuff&echo.test 1285235d&echo.thing & echo.line4 & echo stuff&echo.test 98765&echo.thing)> tempfile.txt"
			subprocess.call(output, shell = True)
		with open('tempfile.txt') as infile:
			# change to open('/home/hofstra /Downloads/tempfile.txt')
			copy = False 
			for line in infile:
				if 'Query: /home/admin/Downloads/offsets.qc' in line:
					copy= True  # these lines pull only the line before nmatchedterms
				elif '..nmatchableterms:' in line:						
					copy = False 	# stops at the line after nmatchedterms
				elif copy:
					self.vectorlist.append(line.strip('..nstringsmatched: '))
						#print(self.vectorlist) # strips the uneccessary things so only the number is left
		subprocess.call(deletetemp, shell = True)		
							# and inserts it into vectorlist at the appropriate index.
		self.vectorlist= list(set(self.vectorlist))
		
#####################################################################################


	def exportlist(self):  
		location = str(self.queryfile).strip("query.txt") + "trainingfile.txt"		
		file = open(location,'a+')
		#strip_list= list(map(str.split('\n'), self.vectorlist))
		for i in range (len(self.vectorlist)):
			self.vectorlist[i] = re.sub('[^0-9]', '', self.vectorlist[i]) 
		#print(self.vectorlist) # prints same as strip_list # makes it a string
		file.write('[')
		for i in range (len(self.vectorlist)):
			trainoutput= self.vectorlist[i]+ ', ' 
			file.write(trainoutput)
		file.write('0] \n')
		file.write(
		file.close()

#####################################################################################

trump = VectorModel('donaldquery.txt')
trump.populatelist()
# NEED TO ADD FOR LOOP TO CYCLE THROUGH PARSED FILE
trump.createlist('parsedfile2.txt')
trump.exportlist()

bernie = VectorModel("berniequery.txt")
bernie.populatelist()
bernie.createlist("parsedfile2.txt")
bernie.exportlist()

hillary = VectorModel("hillaryquery.txt")
hillary.populatelist()
hillary.createlist("parsedfile2.txt")
hillary.exportlist()

#print(s.querylist)

#print(s.queryfile)


