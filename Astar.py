import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node, x, y):
        if node not in self.graph:
            self.graph[node] = {'coordinates': (x, y), 'neighbors': {}}

    def add_edge(self, node1, node2, weight):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1]['neighbors'][node2] = weight
            self.graph[node2]['neighbors'][node1] = weight

    def get_neighbors(self, node):
        if node in self.graph:
            return self.graph[node]['neighbors']
        else:
            return None

    def get_coordinates(self, node):
        if node in self.graph:
            return self.graph[node]['coordinates']
        else:
            return None

    def get_edge_weight(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            if node2 in self.graph[node1]['neighbors']:
                return self.graph[node1]['neighbors'][node2]
        return None

def calculate_heuristic(current_node, goal_node, graph, f, global_node):
    current_coordinates = graph.get_coordinates(current_node)
    goal_coordinates = graph.get_coordinates(goal_node)
    edge_weight = graph.get_edge_weight(global_node, current_node)
    if edge_weight is not None:
        node_f = f + edge_weight
    else:
        node_f = float('inf')  # Assigning a large value for edge weight to make it unreachable
    return abs(current_coordinates[0] - goal_coordinates[0]) + abs(current_coordinates[1] - goal_coordinates[1]), node_f


def best_first_search(graph, start_node, goal_node):
    visited = set()
    global_node = start_node
    start_total_heuristic, start_node_f = calculate_heuristic(start_node, goal_node, graph, 0, global_node)
    priority_queue = [(start_total_heuristic, start_node_f, start_node, 0)]  # (total heuristic value, f value, node, g value)
    while priority_queue:
        total_h, node_f, current_node, g_value = heapq.heappop(priority_queue)
        if current_node == goal_node:
            return True, g_value  # Goal reached
        global_node = current_node

        if current_node not in visited:
            visited.add(current_node)
            neighbors = graph.get_neighbors(current_node)
            for neighbor, weight in neighbors.items():
                neighbor_heuristic, neighbor_f = calculate_heuristic(neighbor, goal_node, graph, node_f, global_node)
                heapq.heappush(priority_queue, (total_h + neighbor_heuristic, neighbor_f, neighbor, g_value + weight))

    return False, None  # Goal not reachable

# Function to take input for graph data
def input_graph():
    g = Graph()
    num_nodes = int(input("Enter the number of nodes in the graph: "))
    for i in range(num_nodes):
        node_name = input(f"Enter node {i + 1} name: ")
        x, y = map(int, input(f"Enter coordinates (x, y) for node {node_name}: ").split())
        g.add_node(node_name, x, y)
    
    num_edges = int(input("Enter the number of edges in the graph: "))
    for i in range(num_edges):
        node1, node2, weight = input(f"Enter edge {i + 1} (node1 node2 weight): ").split()
        weight = int(weight)
        g.add_edge(node1, node2, weight)
    
    return g

# Take input for start and goal nodes
start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")

# Hardcoded graph data
g = input_graph()

found, g_value = best_first_search(g, start_node, goal_node)
if found:
    print(f"Goal node '{goal_node}' reached from start node '{start_node}'.")
    print("Path:")
    print(goal_node, f"G: {g_value}")
    current_node = goal_node
    while current_node != start_node:
        neighbors = g.get_neighbors(current_node)
        for neighbor, weight in neighbors.items():
            if g_value - weight == g.get_edge_weight(neighbor, current_node):
                print(neighbor, f"G: {g_value - weight}")
                current_node = neighbor
                break
else:
    print(f"Goal node '{goal_node}' not reachable from start node '{start_node}'.")
