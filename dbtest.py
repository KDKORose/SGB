
from pymongo import MongoClient

uri = "mongodb+srv://kdko:cAM5wqY57DwtneQq@sgb.ulhffyw.mongodb.net/?appName=SGB"

# Create a new client and connect to the server
client = MongoClient(uri, tls=True, tlsAllowInvalidCertificates=True)

# Send a ping to confirm a successful connection
try:
    database = client["scandal"]
    collection = database["config"]

    results = collection.find({})
    for document in results:
        print(document)

    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)