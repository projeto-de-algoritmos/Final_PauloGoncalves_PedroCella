from collections import defaultdict
from utils import pd
import math

class Node:
  def __init__(self, name, tarefas: list):
      self.nome = name
      self.TarefasDoNode = tarefas
      self.distancia = math.inf
      self.path = list()

class Elo:
  def __init__(self, nodePai: Node, nodeFilho: Node, distancia: float):
    self.nodePai = nodePai
    self.nodeFilho = nodeFilho
    self.distancia = distancia

class Grafo:
  def __init__(self, isDirected: bool = False) -> None:
    self.nodes = list()
    self.elos = list()
    self.isDirected = isDirected	
  
  def buildTarefasDic(self):
    self.tarefasParaNodes = dict()
    self.todasTarefas = list()

    for node in self.nodes:
      for tarefa in node.TarefasDoNode:
        self.tarefasParaNodes.update({tarefa: node})
        self.todasTarefas.append(tarefa)
        
  def getChoices(self):
    self.buildTarefasDic()

    self.choices = pd.pd(self.todasTarefas)
    self.choices.intervalSchWei()
    
  def addNode(self, node: Node):
    self.nodes.append(node)

  def getElos(self, node: Node):
    """
    Função para poder retornar os nodes que estão conectados ao um certo Node
    """
    adjList = []

    for Elo in self.elos:
      if Elo.nodePai.nome == node.nome and Elo.nodeFilho.nome not in adjList:
        adjList.append(Elo.nodeFilho)

    return adjList
  def addElo(self, currentNode: Node, nextNode: Node, distancia: float):
    """ Criação de um elo entre 2 Nodes, os salvando em uma lista de Elos
        e adicionando os novos nodes no dicionario de Nodes existentes.
    """
    nodeNames = [x.nome for x in self.nodes]

    try:
      currentNode = self.nodes[nodeNames.index(currentNode.nome)]
    except IndexError:
      self.addNode(currentNode)

    try:
      nextNode = self.nodes[nodeNames.index(nextNode.nome)]
    except IndexError:
      self.addNode(nextNode)
    

    ElosList = [(i.nodePai, i.nodeFilho) for i in self.elos]


    if self.isDirected:
      if (currentNode, nextNode) not in ElosList:
        self.elos.append(Elo(currentNode, nextNode, distancia))
    else:
      if (currentNode, nextNode) not in ElosList and (nextNode, currentNode) not in ElosList:
        self.elos.append(Elo(currentNode, nextNode, distancia))
        self.elos.append(Elo(nextNode, currentNode, distancia))
  
  def getPath(self, nodeA:Node, nodeB:Node):
    for node in self.nodes:
      node.distancia = math.inf
      node.path = list()
      
    nodeB.path.append(nodeA)
    self.bellmanFord(nodeA)

    nodeB.path.append(nodeB)

    return nodeB


  def bellmanFord(self, nodeComeco:Node):
    try: 
      self.nodes[self.nodes.index(nodeComeco)].distancia = 0
      # self.nodes[self.nodes.index(nodeComeco)].path.append(nodeComeco) 
    except IndexError:
      print("Não tem esse node no grafo.")
      return None
    
    for _ in range(len(self.nodes) - 1):
      for elo in self.elos:
        if elo.nodePai.distancia != math.inf and elo.nodePai.distancia + elo.distancia < elo.nodeFilho.distancia:
          elo.nodeFilho.distancia = elo.nodePai.distancia + elo.distancia
          elo.nodeFilho.path += elo.nodePai.path


    for _ in range(len(self.nodes) - 1):
      for elo in self.elos:
        if elo.nodePai.distancia != math.inf and elo.nodePai.distancia + elo.distancia < elo.nodeFilho.distancia:
          return