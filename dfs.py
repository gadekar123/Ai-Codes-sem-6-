from collections import deque

graph = {
    0: [1, 2],
    1: [2, 3, 4],
    2: [0, 3],
    3: [1, 2, 4],
    4: [1, 3]
}

def dfs(graph, start):
  

    visited = set()  # Keep track of visited vertices
    queue = deque([start])  # Use a deque for efficient stack operations

    while queue:
        vertex = queue.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=" ")

            for neighbor in graph[vertex]:
                queue.append(neighbor)

# Perform DFS traversal starting from vertex 0
print("dfs traversal (starting from vertex 0):")
dfs(graph, 0)