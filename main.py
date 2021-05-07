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


grafo.getChoices()


#  Tem q colocar o localização
#  Colocar as tarefas dessa localização
#  Colocar as distancias de cada node




