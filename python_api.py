import pymongo

# Python code to illustrate 
# inserting data in MongoDB 
from pymongo import MongoClient 

try: 
	conn = MongoClient() 
	print("Connected successfully!!!") 
except: 
	print("Could not connect to MongoDB") 

# database 
db = conn.facebook_api 

def insertData(record):
# Insert Data 
	collection = db.user
	rec_id1 = collection.insert_one(record) 
	print("Data inserted with record ids",record) 
	#rec_id2 = collection.insert_one(emp_rec2) 



def printRecords():
	# Printing the data inserted 
	cursor = collection.find() 
	for record in cursor: 
		print(record) 
