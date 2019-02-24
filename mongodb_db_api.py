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


def find_collection(collection_name):
	if collection_name =='user':
		return db.user
	
def find_collection_by_name(collection_name):
	return db.get_collection(collection_name)


def save_to_db_collection_by_name(record, collection_name):
# Insert Data 
	#collection = db.user
	
	collection = find_collection_by_name(collection_name)
	collection.insert_one(record) 
	#print("Data inserted with record ids",record) 
	#rec_id2 = collection.insert_one(emp_rec2) 

	

def save_to_db_collection(record, collection_name):
# Insert Data 
	#collection = db.user
	
	collection = find_collection(collection_name)
	collection.insert(record) 
	#print("Data inserted with record ids",record) 
	#rec_id2 = collection.insert_one(emp_rec2) 

def get_all_documents(collection_name):
	collection = find_collection(collection_name)
	# Printing the data inserted 
	cursor = collection.find() 
	return cursor
	
def print_collection(collection_name):
	collection = find_collection(collection_name)
	# Printing the data inserted 
	cursor = collection.find() 
	for record in cursor: 
		print(record) 
