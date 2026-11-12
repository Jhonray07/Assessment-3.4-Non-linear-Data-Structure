"""Assessment 3.3: Graph (SILVA) with BFS and DFS
Name: Jhonray B. Silva | BSIT 2B
"""
from collections import deque

GRAPH = {
    "S": ["I", "L", "V"],
    "I": ["S", "A"],
    "L": ["S", "V"],
    "V": ["S", "L", "A"],
    "A": ["I", "V"],
}


def bfs_graph(graph, start):
    visited = {start}
    q = deque([start])
    result = []
    while q:
        v = q.popleft()
        result.append(v)
        for w in graph[v]:
            if w not in visited:
                visited.add(w)
                q.append(w)
    return result


def dfs_graph(graph, v, visited=None, result=None):
    if visited is None:
        visited, result = set(), []
    visited.add(v)
    result.append(v)
    for w in graph[v]:
        if w not in visited:
            dfs_graph(graph, w, visited, result)
    return result


if __name__ == "__main__":
    print("Graph BFS:", " - ".join(bfs_graph(GRAPH, "S")))
    print("Graph DFS:", " - ".join(dfs_graph(GRAPH, "S")))