#Nome: Edilson Claudio Silvestrini Filho
#R.A.: 0017/09-1
#Sala: 4º TADS

# Perguntas: 
# 1) Teste os comandos aprendidos (append, sort, etc) com as outras estruturas (dicionário, tupla e conjuntos). Relate os resultados de cada uma delas.
# 2) Crie uma lista com valores inteiros aleatórios e a ordene de maneira crescente e decrescente. (Dica: Pesquise cópia de listas)
# 3) Crie uma matriz 4x4 em python colocando os valores automaticamente de 0 a 15 nas posições em sequência.
# 4) Crie uma matriz 3x3 e faça um programa que peça pro usuário digitar cada valor da matriz.
# 5) Crie uma matriz de tamanho variável, onde a quantidade de linhas e colunas seja definada pelo usuário e que seja preenchida automaticamente de 0 até o máximo valor possível

# Respostas:
# 01 -0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-

dicionario = {"ID": 1,
              "Nome": "Edilson",
              "Idade": 18}
tupla = (8, 5, 7, 6)
conjunto = [1, 9, 2, 8]

## Teste Dicionario
# dicionario.append(5) A Classe dict não tem este metodo .append(), porém podemos concatenar dicts usando o update!
dicionario.update(DataNascimento="11122003", Nome="Edilson Filho")

# dicionario.insert(3,4) Não há como inserir um novo item em uma deterinada posição justamente pelo fato do dicionario não ter uma "ordem especifica de posições"!

i = dicionario.pop("Idade") # Retorna o valor da chave passada e ambas são retiradas do dicionário! Tambem existe o popitem que faz a mesma coisa, porem um uma chave aleatória!
# print("Sua idade era de", i)

# dicionario.remove(3) A Classe dict não tem este metodo .remove(), porém podemos usar o proprio metodo .pop() seco, ou usar o del, porem como ele pode retornar um erro, vamos coloca-lo num if:
if "DataNascimento" in dicionario:
    del dicionario["DataNascimento"]

# dicionario.sort() A Classe dict não tem este metodo .sort(), porém existem outros "jeitos" para ordenar, seja por For´s ou sorted() que pega apenas as chaves, mas como já dito, não é este o objetivo dos dicionários!

len(dicionario) # Retorna quantos itens tem no dicionario!


## Teste Tupla
# tupla.append(5) Por ter com essencia a caracteristica Imuntavel não aceita inserção após sua declaração!

# tupla.insert(3,4) Por ter com essencia a caracteristica Imuntavel não aceita inserção após sua declaração!

# tupla.pop() Por ter com essencia a caracteristica Imuntavel não aceita remoção após sua declaração!

# tupla.remove(3) Por ter com essencia a caracteristica Imuntavel não aceita remoção após sua declaração!

# tupla.sort() Também não funciona pois ela tem que permanecer a mesma! Mas mesmo sabendo disso e caso queria ordena-la, uma solução seria isso:
tupla = sorted(tupla)

len(tupla) # Retorna quantos itens tem na tupla!


## Teste Conjunto
conjunto.append(5) # add um item no final da lista!
conjunto.insert(3,4) # Insere um conteudo em uma posição especifica!
conjunto.pop(1) # Puxa o conteudo do index informado e o retira da lista!
conjunto.remove(4) # remove um item!
conjunto.sort() # Ordena a lista!
len(conjunto) # Retorna quantos itens tem no conjunto!

print(dicionario)
print(tupla)
print(conjunto)

# Logo, Percebos que o metodo len() é o unico que está presente em todas estruras vetoriais do python


# 02 -0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-

from copy import deepcopy
import random

# Criar uma lista com números entre 1 e 52
listaAleatoria = list(range(1,16))
random.shuffle(listaAleatoria)

listaOrdenadaCrescente = deepcopy(listaAleatoria)
listaOrdenadaDecrescente = deepcopy(listaAleatoria)

listaOrdenadaCrescente.sort()
listaOrdenadaDecrescente.sort(reverse=True)

print("Lista Aleatória:  ", listaAleatoria)
print("Lista Crescente:  ", listaOrdenadaCrescente)
print("Lista Decrescente:", listaOrdenadaDecrescente)


# 03 -0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-

matriz, lista = [], []

for i in range(0, 16):
    lista.append(i)

    if(len(lista) == 4):
        matriz.append(lista)
        lista = []

print(matriz)


# 04 -0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-

matriz, lista = [], []

for i in range(0, 3):
    for j in range(0, 3):
        lista.append(int(input("Digite um que será Armazena na posição " + str(i+1) + ' X ' + str(j+1) + ' : ')))
    matriz.append(lista)
    lista = []

print("x    1  2  3\n")

for i in range(0, 3):
    print(i+1, ' ', matriz[i])
    

# 05 -0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-0-

colunas = int(input("Digite o numero de colunas: "))
linhas = int(input("Digite o numero de linhas: "))

matriz, lista, i = [], [], 0

for j in range(0, linhas):
    for k in range(0, colunas):
        i += 1
        lista.append(i)
    matriz.append(lista)
    lista = []

for i in range(0, linhas):
    print(matriz[i])