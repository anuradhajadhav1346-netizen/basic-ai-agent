import time
from collections import deque


# ============================================================
# BFS ALGORITHM
# ============================================================

def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    nodes_expanded = 0

    while queue:
        node, path = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return path, nodes_expanded

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(
                    (neighbor, path + [neighbor])
                )

    return None, nodes_expanded


# ============================================================
# DFS ALGORITHM
# ============================================================

def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    nodes_expanded = 0

    while stack:
        node, path = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return path, nodes_expanded

        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(
                    (neighbor, path + [neighbor])
                )

    return None, nodes_expanded


# ============================================================
# GRAPH
# ============================================================

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


# ============================================================
# START AND GOAL
# ============================================================

start = 'A'
goal = 'E'       # Goal state is E

# Number of times each algorithm will be tested
runs = 5


# ============================================================
# LISTS TO STORE RESULTS
# ============================================================

bfs_times = []
dfs_times = []

bfs_nodes = []
dfs_nodes = []


# ============================================================
# DISPLAY EXPERIMENT INFORMATION
# ============================================================

print("=" * 60)
print("SLE-2: PROFILING REPORT")
print("BFS VS DFS PERFORMANCE ANALYSIS")
print("=" * 60)

print("\nGraph used:")
print("A -> B, C")
print("B -> D, E")
print("C -> F, G")
print("D -> H")
print("E -> I")
print("F -> J")
print("G -> K")

print("\nStart Node:", start)
print("Goal Node:", goal)

print("\nNumber of Runs:", runs)


# ============================================================
# RUN EXPERIMENT
# ============================================================

for run in range(1, runs + 1):

    # --------------------------------------------------------
    # BFS
    # --------------------------------------------------------

    start_time = time.perf_counter()

    bfs_path, bfs_node_count = bfs(
        graph,
        start,
        goal
    )

    end_time = time.perf_counter()

    bfs_execution_time = (
        end_time - start_time
    ) * 1000

    bfs_times.append(bfs_execution_time)
    bfs_nodes.append(bfs_node_count)


    # --------------------------------------------------------
    # DFS
    # --------------------------------------------------------

    start_time = time.perf_counter()

    dfs_path, dfs_node_count = dfs(
        graph,
        start,
        goal
    )

    end_time = time.perf_counter()

    dfs_execution_time = (
        end_time - start_time
    ) * 1000

    dfs_times.append(dfs_execution_time)
    dfs_nodes.append(dfs_node_count)


    # --------------------------------------------------------
    # DISPLAY CURRENT RUN
    # --------------------------------------------------------

    print("\n")
    print("-" * 60)
    print("RUN", run)
    print("-" * 60)

    print("\nBFS")
    print("Path:", bfs_path)
    print(
        "Execution Time:",
        round(bfs_execution_time, 6),
        "ms"
    )
    print(
        "Nodes Expanded:",
        bfs_node_count
    )

    print("\nDFS")
    print("Path:", dfs_path)
    print(
        "Execution Time:",
        round(dfs_execution_time, 6),
        "ms"
    )
    print(
        "Nodes Expanded:",
        dfs_node_count
    )


# ============================================================
# CALCULATE AVERAGES
# ============================================================

average_bfs_time = sum(bfs_times) / runs
average_dfs_time = sum(dfs_times) / runs

average_bfs_nodes = sum(bfs_nodes) / runs
average_dfs_nodes = sum(dfs_nodes) / runs


# ============================================================
# DISPLAY ALL INDIVIDUAL TIMES
# ============================================================

print("\n")
print("=" * 60)
print("INDIVIDUAL RUN TIMES")
print("=" * 60)

print("\nBFS Times:")
for i, value in enumerate(bfs_times, start=1):
    print(
        "Run",
        i,
        ":",
        round(value, 6),
        "ms"
    )

print("\nDFS Times:")
for i, value in enumerate(dfs_times, start=1):
    print(
        "Run",
        i,
        ":",
        round(value, 6),
        "ms"
    )


# ============================================================
# FINAL RESULTS
# ============================================================

print("\n")
print("=" * 60)
print("FINAL RESULTS")
print("=" * 60)

print("\nBFS RESULTS")
print("-" * 30)

print(
    "Average Execution Time:",
    round(average_bfs_time, 6),
    "ms"
)

print(
    "Average Nodes Expanded:",
    round(average_bfs_nodes, 2)
)

print("\nDFS RESULTS")
print("-" * 30)

print(
    "Average Execution Time:",
    round(average_dfs_time, 6),
    "ms"
)

print(
    "Average Nodes Expanded:",
    round(average_dfs_nodes, 2)
)


# ============================================================
# COMPARISON
# ============================================================

print("\n")
print("=" * 60)
print("COMPARISON")
print("=" * 60)

# Compare execution time

if average_bfs_time < average_dfs_time:

    print(
        "Lower Average Execution Time: BFS"
    )

elif average_dfs_time < average_bfs_time:

    print(
        "Lower Average Execution Time: DFS"
    )

else:

    print(
        "Both algorithms have the same average execution time"
    )


# Compare nodes expanded

if average_bfs_nodes < average_dfs_nodes:

    print(
        "Fewer Nodes Expanded: BFS"
    )

elif average_dfs_nodes < average_bfs_nodes:

    print(
        "Fewer Nodes Expanded: DFS"
    )

else:

    print(
        "Both algorithms expanded the same number of nodes"
    )


# ============================================================
# EXPERIMENT COMPLETED
# ============================================================

print("\n")
print("=" * 60)
print("Experiment completed successfully.")
print("=" * 60)