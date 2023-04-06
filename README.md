# MongoDB Backup & Restore

This repository contains two Python scripts to help you backup and restore MongoDB databases. The scripts use the `mongodump` and `mongorestore` utilities to perform the backup and restore operations.

## Setup

1. Create a `.env` file in the same directory as the scripts with the following content:

MONGO_URI=mongodb://{adminName}:{adminPasswd}@{hostName}:{hostPort}/?authSource=admin

Replace `{adminName}`, `{adminPasswd}`, `{hostName}`, and `{hostPort}` with your actual MongoDB credentials and connection details.

## Usage

To use these scripts, simply run them as described below:

### Backup

Run `mongodbBackup.py` to create a backup of your MongoDB databases. This script will create a local directory named `mongodb_backups` containing the backup data.

```sh
python mongodbBackup.py
```

### Resotre
Run `mongodbRestore.py` to restore the backed-up databases to MongoDB. This script will read the data from the `mongodb_backups` directory and restore it to the server. If a document with the same index exists, it will be overwritten.

```sh
python mongodbRestore.py
```
