from bfs import bfs
from dfs import dfs


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I'],
    'F': ['J'],
    'G': ['K'],
    'H': [],
    'I': [],
    'J': [],
    'K': []
}


start = 'A'
goal = 'K'


bfs_path, bfs_nodes = bfs(graph, start, goal)
dfs_path, dfs_nodes = dfs(graph, start, goal)


print("=" * 60)
print("BFS vs DFS COMPARISON")
print("=" * 60)

print("\nBFS")
print("Path:", bfs_path)
print("Nodes Expanded:", bfs_nodes)

print("\nDFS")
print("Path:", dfs_path)
print("Nodes Expanded:", dfs_nodes)

print("\nCOMPARISON")
print("-" * 60)

print(f"{'Metric':<25}{'BFS':<15}{'DFS':<15}")
print("-" * 60)
print(f"{'Nodes Expanded':<25}{bfs_nodes:<15}{dfs_nodes:<15}")
print(f"{'Py-spy Profile':<25}{'bfs_profile.svg':<15}{'dfs_profile.svg':<15}")
print("-" * 60)