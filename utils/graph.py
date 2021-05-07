from collections import defaultdict
from utils import pd
import math

class Node:
  def __init__(self, name, tarefas: list):
      self.Name = name
      self.TarefasDoNode = tarefas
      self.distance = math.inf
      self.Visited = False

class Elo:
  def __init__(self, nodePai: Node, nodeFilho: Node, distancia: float):
    self.nodePai = nodePai
    self.nodeFilho = nodeFilho
    self.distancia = distancia

class Grafo:
  def __init__(self, isDirected: bool = False) -> None:
    self.Nodes = list()
    self.Elos = list()
    self.isDirected = isDirected	
  
  def buildTarefasDic(self):
    self.tarefasParaNodes = dict()
    self.todasTarefas = list()

    for node in self.Nodes:
      for tarefa in node.TarefasDoNode:
        self.tarefasParaNodes.update({tarefa: node})
        self.todasTarefas.append(tarefa)
        
  def getChoices(self):
    self.buildTarefasDic()

    self.choices = pd.pd(self.todasTarefas)
    self.choices.intervalSchWei()
    for t in self.choices.final:
      for x in t:
        print(x.nome, end=" ")
      print("\n---------")

  def addNode(self, node: Node):
    self.Nodes.append(node)

  def addElo(self, currentNode: Node, nextNode: Node, distancia: float):
    """ Criação de um elo entre 2 Nodes, os salvando em uma lista de Elos
        e adicionando os novos nodes no dicionario de Nodes existentes.
    """
    nodeNames = [x.nome for x in self.Nodes]

    try:
      currentNode = self.Nodes[nodeNames.index(currentNode.Name)]
    except IndexError:
      self.addNode(currentNode)

    try:
      nextNode = self.Nodes[nodeNames.index(nextNode.Name)]
    except IndexError:
      self.addNode(nextNode)
    

    ElosList = [(i.nodePai, i.nodeFilho) for i in self.Elos]
    print(ElosList)

    if self.isDirected:
      if (currentNode, nextNode) not in ElosList:
        self.Elos.append(Elo(currentNode, nextNode, distancia))
    else:
      if (currentNode, nextNode) not in ElosList and (nextNode, currentNode) not in ElosList:
        self.Elos.append(Elo(currentNode, nextNode, distancia))
        self.Elos.append(Elo(nextNode, currentNode, distancia))
  
  def bellmanFord(self, nodeComeco:Node):
      distancias = [math.]
  



# def BellmanFord(graph, V, E, src):
    # V = 5 # Number of vertices in graph
    # E = 8 # Number of edges in graph
#     # Initialize distance of all vertices as infinite.
#     dis = [maxsize] * V
 
#     # initialize distance of source as 0
#     dis[src] = 0
 
#     # Relax all edges |V| - 1 times. A simple
#     # shortest path from src to any other
#     # vertex can have at-most |V| - 1 edges
#     for i in range(V - 1):
#         for j in range(E):
#             if dis[graph[j][0]] + \
#                    graph[j][2] < dis[graph[j][1]]:
#                 dis[graph[j][1]] = dis[graph[j][0]] + \
#                                        graph[j][2]
 
#     # check for negative-weight cycles.
#     # The above step guarantees shortest
#     # distances if graph doesn't contain
#     # negative weight cycle. If we get a
#     # shorter path, then there is a cycle.
#     for i in range(E):
#         x = graph[i][0]
#         y = graph[i][1]
#         weight = graph[i][2]
#         if dis[x] != maxsize and dis[x] + \
#                         weight < dis[y]:
#             print("Graph contains negative weight cycle")
 
#     print("Vertex Distance from Source")
#     for i in range(V):
#         print("%d\t\t%d" % (i, dis[i]))
 
