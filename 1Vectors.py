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
	
	global cx                                               #gets the names of all the files from the specified directory
	global filter                                           # used to iterate through and apply functions to each file
	file_names = []
	for content in os.listdir(directory):
		file_names.append(content)
	file_names = sorted(file_names)
	successmessage1 = "files being retrieved"
	print(successmessage1)
 	

##################################################################################
##################################################################################

class VectorModel:  				                # initialize everything
	def __init__(self, file1):  
		self.querylist = []   
		self.queryfile= file1	
		self.vectorlist= []
				
###################################################################################						
		
		
	def populatelist(self):                                 # writes queries from query file to an array used in createlist()
		with open(self.queryfile) as input:
			#for line in open(filename)
				self.querylist = [line.rstrip('\n') for line in open(self.queryfile)] 
	#	successmessage2 = "populating list for " + str(self.queryfile)
	#	print(successmessage2)

###################################################################################		

 		
	def createlist(self, Parsedfile):                                       # sends commands out to command line to envoke TIPS and get results. 
		
		os.chdir("/home/admin/Downloads/TIPS/core/bin");
	#	os.system('pwd')
		deletetemp = "rm /home/admin/Downloads/tempfile.txt"
		templist ='0'
		self.vectorlist = []  
		for i in range (len(self.querylist)):
			output =('/home/admin/Downloads/TIPS/core/bin/match -f ' + Parsedfile + ' -t '+ str(self.querylist[i]) + ' >> /home/admin/Downloads/tempfile.txt')
			subprocess.call(output, shell = True)
			with open('/home/admin/Downloads/tempfile.txt') as infile:
				# change to open('/home/hofstra/Downloads/tempfile.txt')
				copy = False 
			
				for line in infile:
			#		print("DEBUG USE 200: " + line);
					if 'Query: /home/admin/Downloads/TIPS/core/bin/offsets.qc' in line:
						copy= True                               # these lines pull only the line before nmatchedterms
					elif '..nmatchableterms:' in line:						
						copy = False 	                         # stops at the line after nmatchedterms
					elif copy:
						templist = line.strip('..nstringsmatched: ')
						#templist = list(unique_everseen(templist))
				self.vectorlist.append(templist)
				templist = '0'		
                                                                                        # maintains order while getting rid of duplicates from TIPS multiple print lines 		
			
			subprocess.call(deletetemp, shell = True)		
	#		self.vectorlist = list(unique_everseen(self.vectorlist))


#####################################################################################


	def exportlist(self):
		trainoutput = ''
		location = str(self.queryfile).strip("query.txt") + "1training.txt"		
	#	file = open(location,'a+')
		#strip_list= list(map(str.split('\n'), self.vectorlist))
		for i in range (len(self.vectorlist)):
			self.vectorlist[i] = (re.sub('[^0-9]', '', self.vectorlist[i]))  # prints same as strip_list # makes it a string
		for i in range (len(self.vectorlist)):
			trainoutput= trainoutput+',' +self.vectorlist[i] 
		outfile = open(location, "a+")
		outfile.write(trainoutput[1:])
		outfile.write('\n')
		outfile.close()
		print(trainoutput[1:])


####################################################################################



getfilenames("/home/admin/Downloads/scpedfiles")
x = 0.0
y = float(4* len(file_names))
for name in file_names:                                                 # in a for loop to loop through all of the filenames. 
	name1 = "/home/admin/Downloads/scpedfiles/" + name
	person = VectorModel('/home/admin/Downloads/personquery.txt')
	person.populatelist()
	person.createlist(name)
	person.exportlist()
	print(name1)

#	trump = VectorModel('/home/admin/Downloads/donaldquery.txt')
#	trump.populatelist()
#	trump.createlist(name1)
#	trump.exportlist()
#	x +=1 
#	print('trump')
##	print("Vectors are %" + str(int(100*x/y)) + ' complete')
#
#	bernie = VectorModel('/home/admin/Downloads/berniequery.txt')
#	bernie.populatelist()
#	bernie.createlist(name1)
#	bernie.exportlist()
#	x +=1 
#	print('bernie')
##	print("Vectors are %" + str(int(100*x/y)) + ' complete')
#
#	hillary = VectorModel('/home/admin/Downloads/hillaryquery.txt')
#	hillary.populatelist()
#	hillary.createlist(name1)
#	hillary.exportlist()
#	x +=1 
#	print('hillary')
#	print("Vectors are %" + str(int((100*x/y)) + ' complete')
#
#	ted = VectorModel('/home/admin/Downloads/cruzquery.txt')
#	ted. populatelist()
#	ted.createlist(name1)
#	ted.exportlist()
#	x +=1 
#	print('ted')
#	print("Vectors are %" + str(int(100*x/y)) + ' complete')
#	movefile = 'mv ' + name1 +" /home/admin/Downloads/trainedfiles/"+name
#	subprocess.call(movefile, shell = True)
