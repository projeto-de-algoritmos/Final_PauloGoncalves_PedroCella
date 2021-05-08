from collections import defaultdict
from utils import pd
import math

class Node:
  """
  distancia: A distancia para chegar nele a partir de um node X
  Path: O menor caminho para poder chegar no node a partir de um node x
  """
  def __init__(self, name, tarefas: list):
      self.nome = name
      self.TarefasDoNode = tarefas
      self.distancia = math.inf
      self.path = list()

class Elo:
  """
  Elo entre 2 nodes, e a sua distancia
  """
  def __init__(self, nodePai: Node, nodeFilho: Node, distancia: float):
    self.nodePai = nodePai
    self.nodeFilho = nodeFilho
    self.distancia = distancia

class Grafo:
  def __init__(self, isDirected: bool = False) -> None:
    self.nodes = list() # Lista de nodes pertencente ao grafo
    self.elos = list() # Lista de elos entre nodes
    self.isDirected = isDirected	# Se é um grafo direcionado
      
  def addNode(self, node: Node):
    self.nodes.append(node)

  def addElo(self, currentNode: Node, nextNode: Node, distancia: float):
    """ Criação de um elo entre 2 Nodes, os salvando em uma lista de Elos
        e adicionando os novos nodes no dicionario de Nodes existentes.
    """
    nodeNames = [x.nome for x in self.nodes]

    # Exeções para caso o node em questão não tenha sido adiciondo.
    try:
      currentNode = self.nodes[nodeNames.index(currentNode.nome)]
    except IndexError:
      self.addNode(currentNode)

    try:
      nextNode = self.nodes[nodeNames.index(nextNode.nome)]
    except IndexError:
      self.addNode(nextNode)
    

    # Criando um novo elo entre os novos nodes.
    ElosList = [(i.nodePai, i.nodeFilho) for i in self.elos]

    # Caso seja direcionado, cria apenas uma ligação entre os nodes
    if self.isDirected:
      if (currentNode, nextNode) not in ElosList:
        self.elos.append(Elo(currentNode, nextNode, distancia))
    else:
      if (currentNode, nextNode) not in ElosList and (nextNode, currentNode) not in ElosList:
        self.elos.append(Elo(currentNode, nextNode, distancia))
        self.elos.append(Elo(nextNode, currentNode, distancia))
  
  def getElos(self, node: Node):
    """
    Função para poder retornar os nodes que estão conectados ao um certo Node
    """
    adjList = []

    for Elo in self.elos:
      if Elo.nodePai.nome == node.nome and Elo.nodeFilho.nome not in adjList:
        adjList.append(Elo.nodeFilho)

    return adjList

  def getPath(self, nodeA:Node, nodeB:Node):
    """
    """
    for node in self.nodes:
      node.distancia = math.inf
      node.path = list()
    
    self.bellmanFord(nodeA)

    nodeB.path.append(nodeB)

    return nodeB


  def buildTarefasDic(self):
    """
    Função que consetrou um dicionario de tarefas que correspondem ao node que ela está salva.
    """
    self.tarefasParaNodes = dict()
    self.todasTarefas = list()

    for node in self.nodes:
      for tarefa in node.TarefasDoNode:
        self.tarefasParaNodes.update({tarefa: node})
        self.todasTarefas.append(tarefa) # Uma lista com todas as tarefas, de todos os nodes.
        
  def getChoices(self):
    """
    Função com o objetivo de gerar os conjuntos de escolhas, de acordo com as prioridades
    """
    self.buildTarefasDic() # Construindo a lista e dicionario de tarefas.

    self.choices = pd.pd(self.todasTarefas)
    self.choices.intervalSchWei()


  def bellmanFord(self, nodeComeco:Node):
    try: 
      self.nodes[self.nodes.index(nodeComeco)].distancia = 0
    except IndexError:
      print("Não tem esse node no grafo.")
      return None
    
    for _ in range(len(self.nodes) - 1):
      for elo in self.elos:

        if elo.nodePai.distancia != math.inf and elo.nodePai.distancia + elo.distancia < elo.nodeFilho.distancia:
          elo.nodeFilho.distancia = elo.nodePai.distancia + elo.distancia
          elo.nodeFilho.path += elo.nodePai.path
          elo.nodeFilho.path.append(elo.nodePai)

    for _ in range(len(self.nodes) - 1):
      for elo in self.elos:
        if elo.nodePai.distancia != math.inf and elo.nodePai.distancia + elo.distancia < elo.nodeFilho.distancia:
          return