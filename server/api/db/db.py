import pymongo
import certifi
import os

from urllib.parse import quote_plus

username = quote_plus(str(os.environ.get('username')))
password = quote_plus(str(os.environ.get('password')))
cluster = quote_plus(str(os.environ.get('cluster')))

myclient = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@{cluster}.mongodb.net/?retryWrites=true&w=majority", 
                                tlsCAFile=certifi.where())

try:
    print('Database connected!')
except Exception:
    print("Unable to connect to the server.")

#projects -> my database
#project_active -> my collection
db = myclient.get_database('projects')
