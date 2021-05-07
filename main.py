from typing import List
from utils import graph as g, trabalho as t




isDirectional = True if input("Esse grafo é um grafo bi-direcional (s/n): ") == "s" else False

grafo = g.Grafo(isDirectional)
nodes = list()

opcao = "s"
while opcao != "n": # TODO: Mudar para s/n

  nome = input("nome node: ")
  listaTarefas = list()

  LocalizacaoOpcao = "s"  
  while LocalizacaoOpcao != "n":

    nomeTarefa = input("nome: ").split('\r')[0]
    ComecoTarefa = float(input("comeco: "))
    FinalTarefa = float(input("final: "))
    PrioridadeTarefa = float(input("prioridade: "))

    listaTarefas.append(t.trabalho(ComecoTarefa, FinalTarefa, PrioridadeTarefa, nomeTarefa))
    
    LocalizacaoOpcao = input("Continuar colocando tarefas (s/n): ")

  grafo.addNode(g.Node(nome, listaTarefas))
 
  opcao = input("Continuar colocando nodes (s/n):")



for i in grafo.nodes:
  print(f"Escolha em qual node o {i.nome}, se conecta: ")
  opNode = "n"
  while opNode == "n":
    adjNodes = grafo.getElos(i)
    possiveisEscolhas = list()
    for index, j in enumerate(grafo.nodes):
      if i != j and j not in adjNodes:
        possiveisEscolhas.append(index)
        print(f"{index} - {j.nome}")
    nodeEscolhido = -1
    while nodeEscolhido not in possiveisEscolhas and possiveisEscolhas != []:
      nodeEscolhido = int(input(f"Insira o numero do node dejesa colocar a distacia, entre ele e {i.nome}: "))
    if possiveisEscolhas != []:
      distancia = float(input("Insira a distancia: "))

      grafo.addElo(i, grafo.nodes[nodeEscolhido], distancia)

      opNode = input("Deseja parar? (s/n): ")
    else:
      opNode = "s"




grafo.getChoices()

for tarefas in grafo.choices.final:
  # print(tarefas)
  # print(tarefas[0], tarefas[len(tarefas) - 1])
  print(grafo.getDistance(grafo.tarefasParaNodes.get(tarefas[0]), grafo.tarefasParaNodes.get(tarefas[len(tarefas) - 1])).distancia)




