from collections import deque

def bfs(graph, start_node, target_node):
    visited = set()
    queue = deque([start_node])
    
    while queue:
        node = queue.popleft()
        
        if node == target_node:
            return f"Node {target_node} found!"
        
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])
    
    return f"Node {target_node} not found!"

# Example graph (Adjacency List Representation)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Example usage
start = 'A'
target = 'F'
print(bfs(graph, start, target))