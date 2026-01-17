from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise ValueError("MONGO_URI is not set in .env")

# Create a new client and connect to the server
client = MongoClient(MONGO_URI)

# Send a ping to confirm a successful connection
try:
    database = client["scandal"]
    collection = database["config"]

    # Insert a test document
    test_doc = {"name": "Test User", "score": 100}
    insert_result = collection.insert_one(test_doc)
    print(f"Inserted document with _id: {insert_result.inserted_id}")

    # Retrieve the document
    retrieved = collection.find_one({"name": "Test User"})
    print("Retrieved document:", retrieved)

    # Clean up: remove test document
    collection.delete_one({"name": "Test User"})
    print("Test document removed")

    client.close()
except Exception as e:
    print(e)