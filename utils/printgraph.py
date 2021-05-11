import math
import networkx as nx
import matplotlib.pyplot as plt
from utils import graph as g

def printGraph(ownGrafo, visited=[], titulo='Grafo', output='out_img.png'):
    if ownGrafo.isDirected:
        nxGrafo = nx.DiGraph()
    else:
        nxGrafo = nx.Graph()
    
    centerNodes = []
    outerNodes = []

    # converter a grafo do nx
    # nodes e tarefas
    for n in ownGrafo.nodes:
        nxGrafo.add_node(n)
        centerNodes.append(n)
        for t in n.TarefasDoNode:
            nxGrafo.add_node(t)
            outerNodes.append(t)
            nxGrafo.add_edge(n, t)

    # elos entre nodes
    for e in ownGrafo.elos:
        nxGrafo.add_edge(e.nodePai, e.nodeFilho, weight = e.distancia)
    
    # printar com plotlib e draw
    plt.figure(figsize=(12,12)) # tamanho da imagem
    plt.margins(x=0.05,y=0.05)
    rotation = 1.6 * math.pi # <-- mudar se rotação do grafo estiver desalinhada (1.6 para o input2.txt)
    nodePos = nx.shell_layout(nxGrafo, [centerNodes, outerNodes], rotation)
    colorMap = ['#e54f2a' if n.nome in visited and n in centerNodes
                else '#e42f2f' if n.nome in visited
                else '#5ea0cf' if n in centerNodes
                else '#7165c8'
                for n in nxGrafo.nodes]

    # grafo
    nx.draw(nxGrafo,
            with_labels = False,
            node_color = colorMap,
            node_size = [2500 if n in centerNodes else 1000 for n in nxGrafo.nodes],
            pos = nodePos)

    # labels
    for n, (x,y) in nodePos.items():
        yPos = y-0.12
        if n in centerNodes:
            yPos = y-0.17
        plt.text(x, yPos, n.nome, ha='center', va='center')

    # título
    plt.text(0, 1.225, titulo, fontsize=24, ha='center', va='center')

    # salvar output
    plt.savefig("./plots/" + output)