import os
import subprocess

from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables from the .env file
load_dotenv()

# Set up connection string and credentials from the environment variable
uri = os.environ["MONGO_URI"]
client = MongoClient(uri)

# Set backup directory
backup_dir = "mongodb_backups"

# Check if the backup directory exists
if not os.path.exists(backup_dir):
    print(f"Backup directory '{backup_dir}' not found.")
    exit(1)

# Get a list of database backup directories
backup_dirs = os.listdir(backup_dir)

# Loop through each backup directory and restore the database using mongorestore
for db_backup_dir in backup_dirs:
    # Exclude files that are not valid MongoDB database directories (e.g., .DS_Store)
    if db_backup_dir.startswith("."):
        continue

    backup_path = os.path.join(backup_dir, db_backup_dir)
    command = f"mongorestore --drop --uri={uri} --nsInclude={db_backup_dir}.* {backup_path}"

    # Run the command and capture the output
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # Display the output
    print(stdout.decode('utf-8'))
    print(stderr.decode('utf-8'))

print(f"All databases restored from {backup_dir}")