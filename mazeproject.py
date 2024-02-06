#Jasmine B. McCrary


import sys
import networkx as nx

def inputForGraph(filename):
    with open(filename, 'r') as file:
        n, m = map(int, file.readline().split()) #read the num of nodes and num of edges and converts them to int
        roomColors = file.readline().split()#read the color of nodes
        s1, s2 = map(lambda x: int(x)-1, file.readline().split()) #read starting position for rocket and lucky
        edges = [tuple(line.strip().split()) for line in file.readlines()] #read edges from input
    startNode = (s1, s2) #initiate start node for the graph
    return n, m, roomColors, startNode, edges

def createGraph(n, roomColors, edges):
    g = nx.MultiDiGraph()
    
    #add node after reading from input
    for node in range(n):
        g.add_node(node, color=roomColors[node] if node < n - 1 else "W")
    #add the edges from input into the graph
    for first, second, color in edges:
        g.add_edge(int(first) - 1, int(second) - 1, color=color)
    
    return g

def stateGraph(g, startNode, n):
    stateG = nx.DiGraph()
    
    #goal node
    goalN = 'goal'
    stateG.add_node(goalN)
    
    #implement all the states 
    for s1 in range(n):
        for s2 in range(n):
            stateG.add_node((s1, s2))
            
            #if the possible node leads to goal node
            if s1 == n-1 or s2 == n-1:
                stateG.add_edge((s1, s2), goalN)
    
    #add possible edges between all possible nodes
    for possibleEdge in g.edges(keys=True):
        for possibleNode in g.nodes():
            #check the condition
            if g.edges(keys=True)[(possibleEdge)]['color'] == g.nodes()[possibleNode]['color']:
                stateG.add_edge((possibleEdge[0], possibleNode), (possibleEdge[1], possibleNode))
                stateG.add_edge((possibleNode, possibleEdge[0]), (possibleNode, possibleEdge[1]))
    
    return stateG, startNode, goalN

def BFS(stateG, startNode, goalN):
    everyPathSTR = []
    try:
        everyPath = nx.all_shortest_paths(stateG, startNode, goalN)
        
        for path in everyPath:
            outputSTR = ""
            for o in range(len(path)):
                if o < (len(path) - 2):
                    if path[o][0] != path[o + 1][0]:
                        outputSTR += "R" + str(path[o + 1][0] + 1)
                    if path[o][1] != path[o + 1][1]:
                        outputSTR += "L" + str(path[o + 1][1] + 1)
            everyPathSTR.append(outputSTR)
        return min(everyPathSTR)
    
    except nx.NetworkXNoPath:
        return "NO PATH"

    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py input.txt")
        sys.exit(1)
    filename = sys.argv[1]
    n, m, roomColors, startNode, edges = inputForGraph(filename)
    g = createGraph(n, roomColors, edges)
    stateG, startNode, goalN = stateGraph(g, startNode, n)
    
    shortestPath = BFS(stateG, startNode, goalN)  
    print(shortestPath)
