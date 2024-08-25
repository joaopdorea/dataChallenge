from typing import List
import pandas as pd
import csv


listaDicionarios: List = []


#Função para identificar todas as categorias existentes no conjunto de dados
def identifica_categorias(lista: List) -> set:
    conjunto: set = set()
    for item in lista:
        conjunto.add(item["Categoria"])
    return conjunto



#Função para converter csv em lista de dicionários
def converte_csv_lista(caminho: str) -> List:
    lista: List = []
    dict = csv.DictReader(open(caminho))
    for row in dict:
        lista.append(row)
    return lista

listaDicionarios = converte_csv_lista("data/vendas.csv")


#Função para calcular faturamento total por categoria
def calcula_faturamento_total(lista: List, conjunto: set) -> float:
    novoDict: dict = {}
    
    faturamento: float
    
    for itemSet in conjunto:
        faturamento = 0.0
        for i in range(0, len(lista)):
            if(lista[i]["Categoria"] == itemSet):
                faturamento = faturamento + (int(lista[i]["Quantidade"]) * float(lista[i]["Venda"]))
        novoDict[itemSet] = faturamento
    return novoDict
            
#Função para calcular quantidade de vendas total por categoria
def calcula_vendas_total(lista: List, conjunto: set) -> dict:
    novoDict: dict = {} 
    somaVendas: int
    
    for itemSet in conjunto:
        somaVendas = 0
        for i in range(0, len(lista)):
            if(lista[i]["Categoria"] == itemSet):
                somaVendas = somaVendas + int(lista[i]["Quantidade"])
        novoDict[itemSet] = somaVendas
    return novoDict
            
    



print(f"Quantidade total de vendas:{calcula_vendas_total(listaDicionarios, identifica_categorias(listaDicionarios))}")
print(f"Faturamento total:{calcula_faturamento_total(listaDicionarios, identifica_categorias(listaDicionarios))}")











            


