from typing import List
from utils import graph as g, trabalho as t


opcao = 1
grafo = g.Grafo()

nodes = list()

while opcao != 0:

  nome = input()
  
  listaTarefas = list()

  LocalizacaoOpcao = 1  
  i = 0
  while LocalizacaoOpcao != 0:

    nomeTarefa = input().split('\r')[0]
    ComecoTarefa = float(input())
    FinalTarefa = float(input())
    PrioridadeTarefa = float(input())

    listaTarefas.append(t.trabalho(ComecoTarefa, FinalTarefa, PrioridadeTarefa, nomeTarefa))
    try:
      LocalizacaoOpcao = int(input())
      
    except ValueError as e:
      LocalizacaoOpcao = 1

  grafo.addNode(g.Node(nome, listaTarefas))
  try:
      opcao = int(input())
  except ValueError as e:
      opcao = 1


for i in g.nodes:
  print(f"Escolha em qual node o {i.nome}, se conecta:")
  opNode = 1

  while opNode == 1:
    possiveisEscolhas = list()
    for index, j in enumerate(g.nodes):
      if i != j:
        possiveisEscolhas.append(index)
        print(f"{index} - {j.nome}")
    nodeEscolhido = -1
    while nodeEscolhido not in possiveisEscolhas:
      nodeEscolhido = int(input("Insira o numero do node dejesa colocar a distacia, entre ele e {i.nome}: "))
    


grafo.getChoices()


#  Tem q colocar o localização
#  Colocar as tarefas dessa localização
#  Colocar as distancias de cada node




