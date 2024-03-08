from collections import deque

graph = {
    0: [1, 2],
    1: [2, 3, 4],
    2: [0, 3],
    3: [1, 2, 4],
    4: [1, 3]
}

def bfs(graph, start):
  

    visited = set()  # Keep track of visited vertices
    queue = deque([start])  # Use a deque for efficient queue operations

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")

            for neighbor in graph[vertex]:
                queue.append(neighbor)

# Perform BFS traversal starting from vertex 0
print("BFS traversal (starting from vertex 0):")
bfs(graph, 0)