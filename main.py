from prettytable import PrettyTable
import copy as cp
from utils import graph as g, trabalho as t

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

isBiDirectional = False if input("Esse grafo é um grafo bi-direcional (s/n): ") == "s" else True

grafo = g.Grafo(isBiDirectional)
nodes = list()

tabelaDeTarefas = list()

opcao = "s"
while opcao != "n":

  nome = input("nome node: ")
  listaTarefas = list()

  tabelaDeTarefas.append(PrettyTable(["Nome da Tarefa", "Começo da tarefa", "Termino da tarefa", "Prioridade da Tarefa"]))

  LocalizacaoOpcao = "s"  
  while LocalizacaoOpcao != "n":
    cls()
    print(f"Nova tarefa do node {nome}:")
    nomeTarefa = input("Nome da Tarefa: ").split('\r')[0]
    ComecoTarefa = float(input("Começo da Tarefa: "))
    FinalTarefa = float(input("Fim da Tarefa: "))
    PrioridadeTarefa = float(input("Prioridade da Tarefa: "))

    listaTarefas.append(t.trabalho(ComecoTarefa, FinalTarefa, PrioridadeTarefa, nomeTarefa))

    tabelaDeTarefas[-1].add_row([nomeTarefa, ComecoTarefa, FinalTarefa, PrioridadeTarefa])

    LocalizacaoOpcao = input("Deseja continuar colocando tarefas (s/n): ")

  grafo.addNode(g.Node(nome, listaTarefas))
 
  opcao = input("Deseja continuar colocando nodes (s/n):")

for i in grafo.nodes:
  print(f"Escolha em qual node o {i.nome}, se conecta: ")

  adjNodes = grafo.getElos(i)
  possiveisEscolhas = list()

  for index, j in enumerate(grafo.nodes):
    if i != j and j not in adjNodes:
      possiveisEscolhas.append(index)
      print(f"{index} - {j.nome}")


  nodeEscolhido = -1
  while nodeEscolhido not in possiveisEscolhas and possiveisEscolhas != []:
    tmp = input(f"Insira o número do node que deseja colocar a distâcia, entre ele e {i.nome}, escolha um número ou digite 'n' para nenhum (numero/nenhum(n)): ").split('\r')[0]
    if 'n' == tmp:
      break
    else:
      nodeEscolhido = int(tmp)
      print(nodeEscolhido not in possiveisEscolhas)

  if nodeEscolhido in possiveisEscolhas:
    distancia = float(input("Insira a distancia: "))
    grafo.addElo(i, grafo.nodes[nodeEscolhido], distancia)


grafo.getChoices()

cls()

for index, tabela in enumerate(tabelaDeTarefas):
  print(f"Tarefas do node {grafo.nodes[index].nome}:")
  print(tabela, end="\n\n")


for index, tarefas in enumerate(grafo.choices.final):
  caminhoParaConcluirTarefas = list()
  for i in range(0, len(tarefas) - 1):
    caminhoParaConcluirTarefas.append(cp.deepcopy(grafo.getPath(grafo.tarefasParaNodes.get(tarefas[i]), grafo.tarefasParaNodes.get(tarefas[i + 1]))))

  tabela = PrettyTable(["Tarefas feitas", "Começa em", "Termina em", "Prioridade total", "Caminho feito", "Distancia pecorrida"])

  pathTotal = list()
  for caminho in caminhoParaConcluirTarefas:
    for t in caminho.path:
      pathTotal.append(t.nome)
    pathTotal.append("\n")
  
  pathTotal = ",".join(pathTotal)
  if "\n" in pathTotal:
    pathTotal = pathTotal[0: pathTotal.index("\n") + 1] + pathTotal[pathTotal.index("\n") + 2:]
  if pathTotal == "":
    pathTotal = grafo.tarefasParaNodes.get(tarefas[0]).nome
    
  tabela.add_row([",".join([x.nome for x in tarefas]), tarefas[0].comeco, tarefas[-1].final, sum([x.prioridade for x in tarefas]), pathTotal, sum([x.distancia for x in caminhoParaConcluirTarefas])])
  print(f"Para a {index + 1}º escolha de tarefas a serem feitas: ")
  print(tabela)





