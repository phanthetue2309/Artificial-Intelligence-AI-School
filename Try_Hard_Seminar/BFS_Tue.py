import graph2 as Graph

def BFS(tree, initialState, goalTest):
    frontier = []
    frontier.append(initialState)
    explored = []
    while len(frontier) > 0:
        print("Frontier >> ", frontier)     
        state = frontier.pop(0) # xét điểm đầu tiên trong hàng đợi
        state_node = Graph.Node(state)
        explored.append(state)
        print("Explored >> ", explored)  # các đỉnh đã duyệt 

        if goalTest == state:
            return True
        index_state = tree.get_index(state_node)
        for neighbor in tree.nodes[index_state].get_children():
            if neighbor not in list(set(frontier + explored)):
                frontier.append(neighbor)
    return False


if __name__ == "__main__":
    tree = Graph.Graph()
    tree.add_node("S")
    tree.add_node_from(["S", "A", "B", "C", "D", "E", "F", "G", "H"])
    print(tree.show_nodes())

    tree.add_edges_from(
        [
            ("S", "A"),  # thêm vào tọa độ 2 điểm có trọng số
            ("S", "B"),
            ("S", "C"),
            ("A", "D"),
            ("B", "D"),
            ("B", "G"),     
            ("B", "E"),
            ("C", "E"),
            ("D", "F"),
            ("E", "H"),
            ("F", "E"),
            ("H", "G"),
            ("F", "G"),
        ]
    )
    result = BFS(tree, "S", "G")
    print(result)

    # print("=============================")
    # print("Use readfile")
    # print("=============================")

    # tree = Graph.Tree()

    # # From file
    # data = Graph.read_file("bfs.txt")
    # Graph.map_data_to_tree(tree, data)
    # print(tree.show_nodes())
    # result = BFS(tree, 0, 7)
    # print(result)

  