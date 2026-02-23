from pymongo import MongoClient
from urllib.parse import quote_plus

username = "Your Username Here"
password = quote_plus("Your Password Here")
dbName = "stocks_data"

uri = f"mongodb+srv://{username}:{password}@cluster0.wzr6r9y.mongodb.net/{dbName}?retryWrites=true&w=majority"
client = MongoClient(uri, tls=True, tlsAllowInvalidCertificates=True)
db = client[dbName]
stocks_collection = db["stocks_data_collection"]

print(" Connected to MongoDB Atlas successfully!",client.server_info())
# Insert a test stock
stock = {"symbol": "AAPL", "id": "1", "price": 150}
stocks_collection.insert_one(stock)
print("Stock inserted successfully!")
