import csv
import MySQLdb

filename="/home/admin/Downloads/retrieveTest.csv"

mydb = MySQLdb.connect(host='127.0.0.1', user='root', passwd='', db='Twitter')
cursor = mydb.cursor()

dump_writer = csv.writer(open(filename,'w'), delimiter=',',quotechar="'")

query = ("SELECT * FROM TBL_caseData WHERE caseID = 1")
cursor.execute(query)

for row in cursor.fetchall():
	dump_writer.writerow(row)

mydb.commit()
cursor.close()
mydb.close()
print "SUCCESS"
                 
