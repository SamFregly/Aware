import csv
import MySQLdb

mydb = MySQLdb.connect(host='127.0.0.1', user='root', passwd='', db='Twitter')
cursor = mydb.cursor()

csv_data = csv.reader(file('/home/admin/Downloads/UserA/graphpredictions.csv'))
for row in csv_data:

	cursor.execute('INSERT INTO TBL_Prediction(date, value, caseID) VALUES(%s, %s, %s)', row)

mydb.commit()
cursor.close()
mydb.close()
print "SUCCESS"
