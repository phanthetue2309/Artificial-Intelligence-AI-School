import graph_Tue as Graph


def BFS(tree, initialState, goalTest):
    frontier = []
    frontier.append(initialState)
    explored = []
    while len(frontier) > 0:
        print("Frontier >> ", frontier)
        state = frontier.pop(0)  # xét điểm đầu tiên trong hàng đợi
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
    tree = Graph.Tree()
    tree.add_node("S")
    tree.add_node_from(["S", "A", "B", "C", "D", "E", "F", "G", "H"])
    tree.add_edges_from(
        [
            ("S", "A"),  
            ("S", "B"),
            ("S", "C"),
            ("A", "D"),
            ("A", "B"),
            ("B", "C"),
            ("B", "D"),
            ("B", "F"),
            ("B", "G"),
            ("C", "F"),
            ("D", "F"),
            ("D", "E"),
            ("E", "G"),
            ("F", "E"),
            ("H", "G"),
        ]
    )
    result = BFS(tree, "S", "G")
    print(result)
