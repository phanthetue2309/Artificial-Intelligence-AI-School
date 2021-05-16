from csv import excel
from .graph2 import Node, Graph
import pandas as pd
# Đề bài: không gian trạng thái bt 1
def dfs(initial_state, destination_state):
    frontier = list()
    frontier.append(initial_state)
    explored = []
    i = 1
    df = pd.DataFrame(columns=["Frontier", "Explored"])
    pd.set_option("max_colwidth", None)  # ko set max width cua 1 cot
    while len(frontier) > 0:
        state = frontier.pop()
        explored.append(state)
        to_append = [
            list(map(lambda x: x.get_label(), frontier)),
            list(map(lambda x: x.get_label(), explored))
        ]
        series = pd.Series(to_append, index=df.columns)
        df = df.append(series, ignore_index=True)
        if destination_state == state:
            print(df)
            return True
        for neighbor in state.neighbors():
            if neighbor.get_label() not in list(set([e.get_label() for e in frontier + explored])):
                frontier.append(neighbor)
    print(df)
    return False
if __name__ == "__main__":
    graph = Graph()
    # -----------------------------------------------------
    # Add Node manually
    graph.add_node("S")
    graph.add_node_from(["S", "A", "B", "C", "D", "E", "F", "G", "H"])
    graph.add_edges_from(
        [
            ("S", "C", 2),
            ("S", "B", 6),
            ("S", "A", 3),
            ("A", "D", 3),
            ("B", "D", 4),
            ("B", "G", 9),
            ("B", "E", 2),
            ("C", "E", 1),
            ("D", "F", 5),
            ("E", "H", 5),
            ("F", "E", 6),
            ("H", "G", 8),
            ("F", "G", 5),
        ],
        is_duplicated=True  # Bỏ qua hướng của các đường đi
    )
    result = dfs(graph.nodes[0], graph.nodes[7])
    # In kết quả có tìm ra đường đi hay ko
    print(result)
