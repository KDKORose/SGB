from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

class MongoService:
    def __init__(self):
        self.uri = os.getenv("MONGO_URI")
        if not self.uri:
            raise ValueError("MONGO_URI is not set in environment")

        self.client: MongoClient | None = None

    def connect(self):
        self.client = MongoClient(self.uri, serverSelectionTimeoutMS=5000)

        # Force a connection test
        self.client.admin.command("ping")
        print("MongoDB connected successfully")

    def close(self):
        if self.client:
            self.client.close()
            print("MongoDB connection closed")
