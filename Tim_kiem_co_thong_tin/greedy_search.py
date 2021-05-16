from graph2 import Node, Graph
import heapq
import pandas as pd

def find_by_label(array_of_node, node):
    for idx, n in enumerate(array_of_node):
        if n == node:
            return idx
    return -1

def update_frontier(frontier, new_node):    # Update status of frontier
    index = find_by_label(frontier, new_node)   
    if index >= 0:
        if frontier[index] > new_node:
            frontier[index] = new_node

def greedy_best_first_search(initial_state, goalTest):
    frontier = list()
    explored = list()
    heapq.heapify(frontier) 
    heapq.heappush(frontier, initial_state)
    df = pd.DataFrame(columns=["Frontier", "Explored"])
    pd.set_option("max_colwidth", None)
    while len(frontier) > 0:
        to_append = [
            list(map(lambda x: x.get_label(), frontier)),
            list(map(lambda x: x.get_label(), explored))
        ]
        
        series = pd.Series(to_append, index=df.columns)
        df = df.append(series, ignore_index=True)
  
        state = heapq.heappop(frontier) 
        print("state =",state)
        explored.append(state)
        if state == goalTest:
         
            print(df)
            return True
        for neighbor in state.neighbors():
            if neighbor.get_label() not in list(set([node.get_label() for node in frontier + explored])):
                heapq.heappush(frontier, neighbor)
            elif find_by_label(array_of_node=frontier, node=neighbor) >= 0:
                update_frontier(frontier=frontier, new_node=neighbor) 
    return False

    
if __name__ == "__main__":
    graph = Graph()
    graph.add_node_from(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"])
    graph.add_edges_from(
        [
            ("A", "B"),
            ("A", "C"),
            ("A", "D"),
            ("B", "E"),
            ("B", "F"),
            ("C", "G"),
            ("C", "H"),
            ("D", "I"),
            ("D", "J"),
            ("F", "K"),
            ("F", "L"),
            ("F", "M"),
            ("H", "N"),
            ("H", "O"),
        ],
    )
    # initial setup
    graph.nodes[0].goal_cost = 6  # goal_cost of node A = 6
    graph.nodes[1].goal_cost = 3  # goal_cost of node B = 3
    graph.nodes[2].goal_cost = 4  # goal_cost of node C = 4
    graph.nodes[3].goal_cost = 5  # goal_cost of node D = 5
    graph.nodes[4].goal_cost = 3  # goal_cost of node E = 3
    graph.nodes[5].goal_cost = 1  # goal_cost of node F = 1
    graph.nodes[6].goal_cost = 6  # goal_cost of node G = 6
    graph.nodes[7].goal_cost = 2  # goal_cost of node H = 2
    graph.nodes[8].goal_cost = 5  # goal_cost of node I = 5
    graph.nodes[9].goal_cost = 4  # goal_cost of node J = 4
    graph.nodes[10].goal_cost = 2  # goal_cost of node K = 2
    graph.nodes[11].goal_cost = 0  # goal_cost of node L = 0
    graph.nodes[12].goal_cost = 4  # goal_cost of node M = 4
    graph.nodes[13].goal_cost = 0  # goal_cost of node N = 0
    graph.nodes[14].goal_cost = 4  # goal_cost of node O = 4
    graph.set_compare_mode(Node.GOAL_COST)  # call func set_compare_mode in graph2 
    result = greedy_best_first_search(initial_state=graph.nodes[0], goalTest=graph.nodes[11])