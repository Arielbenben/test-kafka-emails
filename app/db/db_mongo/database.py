from pymongo import MongoClient
from app.settings.mongo_config import MONGO_DB_URL


client = MongoClient(MONGO_DB_URL)


emails_db = client['emails']
all_emails_collection = emails_db['all_emails']

