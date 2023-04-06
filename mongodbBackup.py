import os
import subprocess
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Set up connection string and credentials from the environment variable
uri = os.environ["MONGO_URI"]
client = MongoClient(uri)

# Connect to MongoDB and list all database names
db_names = client.list_database_names()

# Set backup directory
backup_dir = "mongodb_backups"

if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)

# Loop through each database and create a backup using mongodump
for db_name in db_names:
    backup_path = os.path.join(backup_dir, db_name)
    command = f"mongodump --uri={uri} --db={db_name} --out={backup_path}"
    subprocess.call(command, shell=True)

print(f"All databases backed up to {backup_dir}")