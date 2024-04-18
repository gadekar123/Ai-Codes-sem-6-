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

def calculate_heuristic(current_node, goal_node, graph):
    current_coordinates = graph.get_coordinates(current_node)
    goal_coordinates = graph.get_coordinates(goal_node)
    return abs(current_coordinates[0] - goal_coordinates[0]) + abs(current_coordinates[1] - goal_coordinates[1])

def best_first_search(graph, start_node, goal_node):
    visited = set()
    priority_queue = [(start_node_f, start_node_g, start_node)]  # (heuristic value, node)
    
    while priority_queue:
        f , g , current_node = heapq.heappop(priority_queue)
        if current_node == goal_node:
            return True  # Goal reached
        
        if current_node not in visited:
            visited.add(current_node)
            neighbors = graph.get_neighbors(current_node)
            for neighbor, weight in neighbors.items():
                heapq.heappush(priority_queue, (calculate_heuristic(neighbor, goal_node, graph  ), neighbor))
    
    return False  # Goal not reachable

# Hardcoded graph data
g = Graph()
g.add_node('A', 0, 0)
g.add_node('B', 1, 2)
g.add_node('C', 3, 1)
g.add_edge('A', 'B', 5)
g.add_edge('B', 'C', 3)
g.add_edge('C', 'A', 2)

start_node = 'C'
goal_node = 'A'
start_node_f = 0
start_node_coordinates = g.get_coordinates(start_node)
start_node_g = start_node_coordinates[0] + start_node_coordinates[1]
if best_first_search(g, start_node, goal_node):
    print(f"Goal node '{goal_node}' reached from start node '{start_node}'.")
else:
    print(f"Goal node '{goal_node}' not reachable from start node '{start_node}'.")
