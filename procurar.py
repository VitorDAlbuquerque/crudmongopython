from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['FATEC']
collection = db['NBA']

def search_mongodb(field, value):
    query = {field:{"$regex":value , "$options": "i"}}

    results = collection.find(query)
    return list(results)

    print ( "pesquise no mongo")
    campo = input("Digite o nome do campo")
    valor = input("DIgite o valor pra pesquisar")


    resultado = search_mongodb(campo, valor)
    print("Resultado")
    for doc in resultado:
        print(doc)
        