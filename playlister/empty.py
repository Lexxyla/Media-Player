# Python program to illustrate
# delete, drop and remove
from pymongo import MongoClient

try:
	conn = MongoClient()
	print("Connected successfully!!!")
except:
	print("Could not connect to MongoDB")

# database
db = conn.database

# Created or Switched to collection names: my_gfg_collection
collection = db.my_gfg_collection

emp_rec1 = {
		"name":"Mr.Geek",
		"eid":24,
		"location":"delhi"
		}
emp_rec2 = {
		"name":"Mr.Shaurya",
		"eid":14,
		"location":"delhi"
		}
emp_rec3 = {
		"name":"Mr.Coder",
		"eid":14,
		"location":"gurugram"
		}

# Insert Data
rec_id1 = collection.insert_one(emp_rec1)
rec_id2 = collection.insert_one(emp_rec2)
rec_id3 = collection.insert_one(emp_rec3)
print("Data inserted with record ids",rec_id1," ",rec_id2,rec_id3)

# Printing the document before deletion
cursor = collection.find()
for record in cursor:
	print(record)

# Delete Document with name : Mr Coder
result = collection.delete_one({"name":"Mr.Coder"})

# If query would have been delete all entries with eid:14
# use this
# result = collection.delete_many("eid":14})

cursor = collection.find()
for record in cursor:
    print(record)
