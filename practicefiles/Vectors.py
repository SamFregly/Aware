from more_itertools import unique_everseen
import re
import string
import time
import os
import sys
import stat
import subprocess
import array
global file_names
global cx

def getfilenames(directory):
	
	global cx
	global file_names
	file_names = []
	for content in os.listdir("/home/admin/Downloads/scpedfiles"):
		file_names.append(content)
	successmessage1 = "files being retrieved"
	print(successmessage1)
 	

##################################################################################
##################################################################################

class VectorModel:  				
	def __init__(self, file1):  
		self.querylist = []   
		self.queryfile= file1	
		self.vectorlist= []
				
###################################################################################						
		
		
	def populatelist(self): #DONE!!!!!!!!!!!!!!!
		with open(self.queryfile) as input:
			#for line in open(filename)
				self.querylist = [line.rstrip('\n') for line in open(self.queryfile)] 
	#	successmessage2 = "populating list for " + str(self.queryfile)
	#	print(successmessage2)

###################################################################################		

 		
	def createlist(self, Parsedfile):
		
		os.chdir("/home/admin/Downloads/TIPS/core/bin");
	#	os.system('pwd')
		deletetemp = "rm /home/admin/Downloads/tempfile.txt"
		templist ='0'
		self.vectorlist = []  
		for i in range (len(self.querylist)):
			output =('/home/admin/Downloads/TIPS/core/bin/match -f ' + Parsedfile + ' -t '+ str(self.querylist[i]) + ' >> /home/admin/Downloads/tempfile.txt')

		#	print(output)	
			#"(echo stuff&echo.test 1285235d&echo.thing & echo.line4 & echo stuff&echo.test 98765&echo.thing)> tempfile.txt"
	#		print(output)
			subprocess.call(output, shell = True)

	#		print("DEBUG ----\n");
	#		os.system("cat /home/admin/Downloads/tempfile.txt");
	#		print("--- END OF DEBUG ----\n");
			with open('/home/admin/Downloads/tempfile.txt') as infile:
				# change to open('/home/hofstra/Downloads/tempfile.txt')
				copy = False 
			
				for line in infile:
			#		print("DEBUG USE 200: " + line);
					if 'Query: /home/admin/Downloads/TIPS/core/bin/offsets.qc' in line:
						copy= True  # these lines pull only the line before nmatchedterms
					elif '..nmatchableterms:' in line:						
						copy = False 	# stops at the line after nmatchedterms
					elif copy:
						templist = line.strip('..nstringsmatched: ')
						#templist = list(unique_everseen(templist))
				self.vectorlist.append(templist)
				templist = '0'		
# maintains order while getting rid of duplicates from TIPS multiple print lines 		
			
	#		subprocess.call(deletetemp, shell = True)		
	#		self.vectorlist = list(unique_everseen(self.vectorlist))


#####################################################################################


	def exportlist(self):
		trainoutput = ''
		location = str(self.queryfile).strip("query.txt") + "1trainingfile.txt"		
	#	file = open(location,'a+')
		#strip_list= list(map(str.split('\n'), self.vectorlist))
		for i in range (len(self.vectorlist)):
			self.vectorlist[i] = (re.sub('[^0-9]', '', self.vectorlist[i]))  # prints same as strip_list # makes it a string
		for i in range (len(self.vectorlist)):
			trainoutput= trainoutput+',' +self.vectorlist[i] 
		file.write(trainoutput)
		file.write('\n')
		file.close()
		print(self.vectorlist)


####################################################################################



getfilenames("/home/admin/Downloads/scpedfile")

for name in file_names:
	x = 0
	y = 4 * len(file_names)
	 
	name = "/home/admin/Downloads/scpedfiles/" + name
	person = VectorModel('/home/admin/Downloads/personquery.txt')
	person.populatelist()
	person.createlist(name)
	person.exportlist()

#	trump = VectorModel('/home/admin/Downloads/donaldquery.txt')
#	trump.populatelist()
#	trump.createlist(name)
#	trump.exportlist()
	x +=1
	print( 'Vectors are %'+ str(y/x) + 'complete' )
#	bernie = VectorModel('/home/admin/Downloads/berniequery.txt')
#	bernie.populatelist()
#	bernie.createlist(name)
#	bernie.exportlist()
	x +=1
	print( 'Vectors are %'+ str(y/x) + 'complete' )
#	hillary = VectorModel('/home/admin/Downloads/hillaryquery.txt')
#	hillary.populatelist()
#	hillary.createlist(name)
#	hillary.exportlist()
	x +=1 		
	print( 'Vectors are %'+ str(y/x) + 'complete' )
#	ted = VectorModel('/home/admin/Downloads/cruzquery.txt')
#	ted. populatelist()
#	ted.createlist(name)
#	ted.exportlist()
	x += 1 
	print( 'Vectors are %'+ str(y/x) + 'complete' )
	
