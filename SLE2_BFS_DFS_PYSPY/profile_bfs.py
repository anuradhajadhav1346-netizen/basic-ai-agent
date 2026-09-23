from bfs import bfs


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


# Repeat the experiment many times
# so py-spy gets enough samples.
for i in range(1000000):
    bfs(graph, start, goal)


print("BFS profiling completed.")