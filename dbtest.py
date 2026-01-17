from pymongo import MongoClient
from dotenv import load_dotenv
import os
import urllib.parse

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise ValueError("MONGO_URI is not set in .env")

# Create a new client and connect to the server


# Send a ping to confirm a successful connection
try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
     # Attempt to fetch databases
    dbs = client.list_database_names()
    print("Connected! Databases:", dbs)
except Exception as e:
    print(e)