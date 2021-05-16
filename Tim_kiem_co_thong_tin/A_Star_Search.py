from graph2 import Node, Graph
import heapq
import pandas as pd

def update_cost(graph, current_node, prev_node):
    if graph.get_edge(prev_node, current_node) is not None:
        #print(graph.get_edge(prev_node, current_node))  # print infor of prev_node and current_node
        if current_node.cost > prev_node.cost + graph.get_edge(prev_node, current_node)[2]:
            current_node.cost = prev_node.cost + graph.get_edge(prev_node, current_node)[2]

def find_by_label(array_of_node, node):
    for idx, n in enumerate(array_of_node):
        if n == node:
            return idx
    return -1

def update_frontier(frontier, new_node):     # Update trạng thái của frontier
    index = find_by_label(frontier, new_node)
    if index >= 0:
        if frontier[index] > new_node:
           frontier[index] = new_node

def a_star_search(graph, initial_state, goalTest):
    frontier = []   # or can use frontier = list()
    explored = []
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
        df = df.append(series, ignore_index=True)   # show the way search 
        state = heapq.heappop(frontier)
        explored.append(state)
        if state == goalTest:
            # sum = 0   # notice : sum need total by sum of weight and goal cost 
            # for i in explored:  # print sum of goal _ cost
            #     sum += i.get_goal_cost()  

            # print("goal cost = " + str(sum))   
            print(df)
            return True
        for neighbor in state.neighbors():
            update_cost(graph, current_node=neighbor, prev_node=state)   # update A* cost of current node
            neighbor.compare_mode = neighbor.cost + neighbor.goal_cost
            if neighbor.get_label() not in list(set([e.get_label() for e in frontier + explored])):
                heapq.heappush(frontier, neighbor)
            elif find_by_label(array_of_node=frontier, node=neighbor) >= 0:
                update_frontier(frontier=frontier, new_node=neighbor)
    return False

if __name__ == "__main__":
    graph = Graph()
    graph.add_node_from(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"])    
    # first you have to add node
    graph.add_edges_from(   # second you have to add edges to graph
        [
            ("A", "B", 2),
            ("A", "C", 1),
            ("A", "D", 3),
            ("B", "E", 5),
            ("B", "F", 4),
            ("C", "G", 6),
            ("C", "H", 3),
            ("D", "I", 2),
            ("D", "J", 4),
            ("F", "K", 2),
            ("F", "L", 1),
            ("F", "M", 4),
            ("H", "N", 2),
            ("H", "O", 4),
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
    graph.nodes[0].cost = 0  # cost tu A -> A = 0
    
    graph.set_compare_mode(Node.A_STAR)
    print("graph nodes End = " + str(graph.nodes[11]))
    #result = a_star_search(graph=graph, initial_state=graph.nodes[0], goalTest=graph.nodes[11])
    # goal_cost of node here is 11 => you can change to another
    result = a_star_search(graph=graph, initial_state=graph.nodes[0], goalTest=graph.nodes[14])

    print(result)
