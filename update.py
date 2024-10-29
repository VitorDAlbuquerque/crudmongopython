from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['FATEC']
collection = db['NBA']


def search_mongodb(field,value):
    query = {field: {"$regex": value, "$options": "i"}}
    results = collection.find(query)
    return list(results)

def update_mongodb(field, old_value, new_value):
    query = {field: {"$regex": old_value, "$options": "i"}}
    update = {"$set": {field:new_value}}
    result = collection.update_many(query, update)

    return result.modified_count

print("Pesquise o mongo")
campo = input("Digite o campo")
valor = input("valor pra pesquisar")

resultado = search_mongodb(campo,valor)
print("Resultado")
for doc in resultado:
    print(doc)

if resultado:
    novo_valor = input(f"Digite o novo valor para {campo}: ")
    mod_count = update_mongodb(campo,valor,novo_valor)
    print(f"{mod_count} documentos atualizaods")

    resultado_atualizado = search_mongodb(campo, novo_valor)
    print("Resultado apos atualização")
    for doc in resultado_atualizado:
        print(doc)
else:
    print("Nenhum documento")