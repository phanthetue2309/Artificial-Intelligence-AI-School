class Node:
    def __init__(self, data):
        self.data = data
        self.parents = []
        self.children = []

    def get_data(self):
        return self.data

    def get_children(self):
        return [node.get_data() for node in self.children]

    def get_parents(self):
        return [node.get_data() for node in self.parents]

class Node_A(Node):
    COST = '__COST__'
    GOAL_COST = '__GOAL_COST__'
    A_STAR = '__A_STAR__'
    def __init__(self, label, cost=100000, goal_cost=100000):
        self.label = label
        self.cost = cost  # for uniform cost search
        self.goal_cost = goal_cost  # for greedy best fit search
        self.compare_mode = Node_A.COST  # set compare mode for specific algorithm
        self.path = []
        self.parents = []
        self.children = []
        self.depth = 0
    # show the information when code print(node)
    def __repr__(self):
        return str(dict({
            "label": self.label,
            "cost": self.cost,
            "goal_cost": self.goal_cost,
        }))
        
    def __hash__(self):
        return hash(self.label)

    def __eq__(self, other):
        return self.label == other.label

    def __lt__(self, other):
        if self.compare_mode is Node_A.COST:
            return self.cost < other.cost
        if self.compare_mode is Node_A.GOAL_COST:
            return self.goal_cost < other.goal_cost
        if self.compare_mode is Node_A.A_STAR:
            return self.cost + self.goal_cost < other.cost + other.goal_cost
        return self.cost < other.cost
  
    def get_goal_cost(self):
        return self.goal_cost
        
    def get_label(self):
        return self.label

    def get_neighbors(self):
        return [node.get_label() for node in self.neighbors()]

    def neighbors(self):    # children + parents
        children = self.children
        parents = self.parents
        neigbors = children + parents
        seen = set()
        neigbors = [x for x in children + parents if not (x in seen or seen.add(x))]
        return neigbors

    def set_compare_mode(self, mode):
        if mode != Node_A.COST and mode != Node_A.A_STAR and mode != Node_A.GOAL_COST:
            self.compare_mode = Node_A.COST
        else:
            self.compare_mode = mode

class Tree:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def clear(self):
        self.nodes = []
        self.edges = []

    def number_of_nodes(self):
        return len(self.nodes)

    def number_of_edges(self):
        return len(self.edges)

    def get_index(self, node):
        for idx, n in enumerate(self.nodes):
            if n.get_data() == node.get_data():
                return idx
        return -1

    def add_node(self, node_name):
        node = Node(node_name)
        if not self.is_contains(node):
            self.nodes.append(node)

    def add_node_from(self, array_of_nodes_name):
        for el in array_of_nodes_name:
            node = Node(el)
            if not self.is_contains(node):
                self.nodes.append(node)

    def is_contains(self, node):
        for el in self.nodes:
            if el.get_data() == node.get_data():
                return True
        return False

    def add_edge(self, start_name, end_name):
        start_node = Node(start_name)
        end_node = Node(end_name)
        if not self.is_contains(start_node):
            self.add_node(start_name)
        if not self.is_contains(end_node):
            self.add_node(end_name)
        start_index = self.get_index(start_node)
        end_index = self.get_index(end_node)

        self.nodes[start_index].children.append(end_node)
        self.nodes[end_index].parents.append(start_node)
        self.edges.append((self.nodes[start_index], self.nodes[end_index]))

    def add_edges_from(self, array_of_tuple_node):
        for tup in array_of_tuple_node:
            start = tup[0]
            end = tup[1]
            self.add_edge(start, end)

    def show_nodes(self):
        return [node.get_data() for node in self.nodes]

    def show_edges(self):
        return [(edge[0].get_data(), edge[1].get_data()) for edge in self.edges]

class Graph(Tree):
    def get_index(self, node):
        for idx, n in enumerate(self.nodes):
            if n == node:
                return idx
        return -1

    def is_contains(self, node):
        for el in self.nodes:
            if el == node:
                return True
        return False

    def add_node(self, label):
        node = Node_A(label)
        if not self.is_contains(node):
            self.nodes.append(node)

    def add_node_from(self, array_of_label):
        for el in array_of_label:
            self.add_node(label=el)

    def add_edge(self, start_label, end_label, weight=10000):
        start_node = Node_A(start_label)
        end_node = Node_A(end_label)
        if not self.is_contains(start_node):
            self.add_node(start_node)
        if not self.is_contains(end_node):
            self.add_node(end_node)

        start_index = self.get_index(start_node)
        end_index = self.get_index(end_node)

        self.nodes[start_index].children.append(self.nodes[end_index])
        self.nodes[end_index].parents.append(self.nodes[start_index])
        self.edges.append((self.nodes[start_index], self.nodes[end_index], weight))

    def add_edges_from(self, array_of_tuple_node, is_duplicated=False):
        for tup in array_of_tuple_node:
            start = tup[0]
            end = tup[1]
            if len(tup) == 3:
                weight = tup[2] or 10000
            else:
                weight = 10000
            self.add_edge(start, end, weight)
            if is_duplicated:
                self.add_edge(end, start, weight)

    def get_edge(self, start_node, end_node):
        try:
            return [edges for edges in self.edges if edges[0] == start_node
                    and edges[1] == end_node][0]
        except:
            return None

    def show_nodes(self):   
        return [node.get_label() for node in self.nodes]

    def show_edges(self):
        return [(edge[0].get_label(), edge[1].get_label(), edge[2]) for edge in self.edges]

    def set_compare_mode(self, mode):
        for node in self.nodes:
            node.set_compare_mode(mode)


def read_file(file_path):
    f = open(file_path)
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    data = []
    for line in lines:
        data.append([int(num) for num in line.split(" ")])
    return data


def map_data_to_tree(tree, data):
    for idx, row in enumerate(data):
        tree.add_node(node_name=idx)
        for idx_col, col in enumerate(row):
            if col == 1:
                tree.add_edge(start_name=idx, end_name=idx_col)