from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['FATEC']
collection = db['NBA']


def search_mongodb(field,value):
    query = {field: {"$regex": value, "$optins": "i"}}
    results = collection.find(query)
    return list(results)

def update_mongodb(field, old_value, new_value):
    query = {field: {"$regex": old_value, "$options": "i"}}
    update = {"$set": {field: new_value}}
    result = collection.update_many(query, update)
    return result.modified_count

def delete_mongodb(field,value):
    query = {field: {"$regex": value, "$options": "i"}}
    result = collection.delete_many(query)
    return result.deleted_count

print("pesquisa no mongodb")
campo = input("DIgite o nome do campo para pesquisar")
valor = input("Digite o valor")


resultado = search_mongodb(campo,valor)
print("REsuytlado")
for doc in resultado:
    print(doc)


if resultado: 
    acao = input("Voce quer atualizar")
    if acao.lower() == "a":
        novo_valor = input(f"digite o novo valor {campo}")
        mod_count = update_mongodb(campo,valor,novo_valor)
        print(f"{mod_count} docuymentos")
        resultado_atualizado = search_mongodb(campo,novo_valor)
        print("Resultado")
        for doc in resultado_atualizado:
            print(doc)
    elif acao.lower == 'e':
        del_count = delete_mongodb(campo,valor)
        print(f"{del_count} documentos exlcluidos")

        resultado_restante = search_mongodb(campo,valor)
        print("resultado apos a exclusão")
        for doc in resultado_restante:
            print(doc)
    else:
        print("nenhum doc achado")
    