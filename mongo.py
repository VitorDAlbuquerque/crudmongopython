import pandas as pd
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['dsmteste']
collection = db['nba']

csv_file = 'NBA.csv'
data = pd.read_csv(csv_file)

data_dict = data.to_dict('records')

collection.insert_many(data_dict)

print("Dados inseridos ")


