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
    print(tree.show_nodes())

    tree.add_edges_from(
        [
            ("S", "A", 3),  # thêm vào tọa độ 2 điểm có trọng số
            ("S", "B", 6),
            ("S", "C", 2),
            ("A", "D", 3),
            ("B", "G", 9),
            ("B", "E", 2),
            ("C", "E", 1),
            ("D", "F", 5),
            ("E", "H", 5),
            ("F", "E", 6),
            ("H", "G", 8),
            ("F", "G", 5),
        ]
    )
    result = BFS(tree, "S", "G")
    print(result)
