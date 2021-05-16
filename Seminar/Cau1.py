from graph_Tue import Node, Graph
import numpy as np
g = Graph()
g.add_node(1)
#Minimax
def MaxValue(node):
    if len(node.children) == 0:
        return node
    node.value = -100000
    for child in node.children:
        temp = MinValue(child)
        if temp.value > node.value:
            node.value = temp.value
    return node
def MinValue(node):
    if len(node.children) == 0:
        return node
    node.value = 100000
    for child in node.children:
        temp = MaxValue(child)
        if temp.value < node.value:
            node.value = temp.value
    return node
def Minimax_Search(state):
     MaxValue(state)
#Tao cay tro choi
def checkValue(ar, ans = 1): #ans = 1 tương ứng O thắng, ans = -1 tương ứng X thắng
    for i in range(0, 3):
        if (ar[i][0] == ar[i][1] and ar[i][0] == ar[i][2] and ar[i][0] == 1):
            return -1 * ans
        elif (ar[i][0] == ar[i][1] and ar[i][0] == ar[i][2] and ar[i][0] == 2):
            return 1 * ans
        elif (ar[0][i] == ar[1][i] and ar[0][i] == ar[2][i] and ar[0][i] == 1):
            return -1 * ans
        elif (ar[0][i] == ar[1][i] and ar[0][i] == ar[2][i] and ar[0][i] == 2):
            return 1 * ans
    if (ar[0][0] == ar[1][1] and ar[0][0] == ar[2][2] and ar[0][0] == 1):
        return -1 * ans
    elif (ar[0][2] == ar[1][1] and ar[0][2] == ar[2][0] and ar[0][2] == 1):
        return -1 * ans
    elif (ar[0][0] == ar[1][1] and ar[0][0] == ar[2][2] and ar[0][0] == 2):
        return 1 * ans
    elif (ar[0][2] == ar[1][1] and ar[0][2] == ar[2][0] and ar[0][2] == 2):
        return 1 * ans
    return 0
def createTree(ar, state, node):
    for i in range(0, 3):
        for j in range(0, 3):
            if (ar[i][j] == 0):
                ar[i][j] = state
                x = g.number_of_nodes()
                g.add_node(x + 1)
                g.add_edge(node, x + 1)
                g.nodes[x].cost = g.nodes[x].value = checkValue(ar)
                print(x + 1)
                print(ar)
                if (g.nodes[x].cost == 1):
                    print("O win")
                elif (g.nodes[x].cost == -1):
                    print("X win")
                if (state == 1):
                    createTree(ar, 2, x + 1)
                else:
                    createTree(ar, 1, x + 1)
                ar[i][j] = 0
#In cay
def printTree(initialState):
    frontier = list()
    explored = []
    frontier.append(initialState)
    while frontier:
        state = frontier.pop()
        if state not in explored:
            explored.append(state)
        print(state)
        for neighbor in state.neighbors():
            if neighbor.get_label() not in list(set([e.get_label() for e in frontier + explored])):
                frontier.append(neighbor)
    return 0
#main
ar = np.array([[0, 0, 0],
              [1, 1, 2],
              [0, 2, 0]])
createTree(ar, 2, 1)

printTree(g.nodes[0])
Minimax_Search(g.nodes[0])
if (g.nodes[0].value == 0):
    print("Dù đánh ở đâu, trò chơi sẽ hoà")
elif (g.nodes[0].value == 1):
    for child in g.nodes[0].children:
        if (child.value == 1):
            print(child.label)
            break
else:
    print("Dù đánh ở đâu, trò chơi sẽ thua")
