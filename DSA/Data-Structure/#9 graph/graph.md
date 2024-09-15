# Graph in Python

A **graph** is a data structure consisting of nodes (vertices) and edges that connect pairs of nodes. Graphs can represent various relationships and are used in algorithms for tasks such as searching, shortest path finding, and network flow.

Graphs can be **directed** (where edges have a direction) or **undirected** (where edges do not have a direction). They can also be **weighted** (where edges have weights) or **unweighted**.

---

## Graph Representation

### 1. Adjacency Matrix

An **adjacency matrix** is a 2D array where the element at row `i` and column `j` represents the presence or weight of an edge between vertex `i` and vertex `j`.

```python
class GraphAdjMatrix:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v, weight=1):
        self.matrix[u][v] = weight
        self.matrix[v][u] = weight  # For undirected graph

    def display(self):
        for row in self.matrix:
            print(row)
```

### 2. Adjacency List

An **adjacency list** represents a graph as a list of lists or dictionaries. Each list or dictionary entry contains the vertices adjacent to a given vertex.

```python
class GraphAdjList:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, u, v, weight=1):
        if u not in self.graph:
            self.add_vertex(u)
        if v not in self.graph:
            self.add_vertex(v)
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # For undirected graph

    def display(self):
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {edges}")
```

---

## Graph Operations

### 1. Depth-First Search (DFS)

**Depth-First Search** (DFS) explores as far as possible along each branch before backtracking.

#### DFS for Adjacency List

```python
class GraphDFS(GraphAdjList):
    def dfs(self, start):
        visited = set()
        self._dfs(start, visited)

    def _dfs(self, vertex, visited):
        if vertex in visited:
            return
        visited.add(vertex)
        print(vertex, end=" ")
        for neighbor, _ in self.graph.get(vertex, []):
            self._dfs(neighbor, visited)
```

### 2. Breadth-First Search (BFS)

**Breadth-First Search** (BFS) explores all neighbors of a vertex before moving on to the next level.

#### BFS for Adjacency List

```python
from collections import deque

class GraphBFS(GraphAdjList):
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex, end=" ")
                for neighbor, _ in self.graph.get(vertex, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
```

---

## Shortest Path Algorithms

### 1. Dijkstra’s Algorithm

**Dijkstra’s Algorithm** finds the shortest path from a single source to all other vertices in a weighted graph with non-negative weights.

#### Dijkstra's Algorithm for Adjacency List

```python
import heapq

class GraphDijkstra(GraphAdjList):
    def dijkstra(self, start):
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            if current_distance > distances[current_vertex]:
                continue
            
            for neighbor, weight in self.graph.get(current_vertex, []):
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances
```

### 2. Bellman-Ford Algorithm

**Bellman-Ford Algorithm** finds the shortest paths from a single source vertex to all other vertices in a graph, and it can handle negative weights.

#### Bellman-Ford Algorithm for Adjacency List

```python
class GraphBellmanFord(GraphAdjList):
    def bellman_ford(self, start):
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0
        
        for _ in range(len(self.graph) - 1):
            for u in self.graph:
                for v, weight in self.graph[u]:
                    if distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight
        
        for u in self.graph:
            for v, weight in self.graph[u]:
                if distances[u] + weight < distances[v]:
                    raise ValueError("Graph contains a negative weight cycle")
        
        return distances
```

---

## Graph Example

Here’s a simple example of creating and using a graph:

```python
# Create a graph
g = GraphAdjList()
g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 4)
g.add_edge('B', 'C', 2)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 1)

# Display the graph
g.display()

# Perform BFS and DFS
print("DFS:")
g_dfs = GraphDFS()
g_dfs.graph = g.graph
g_dfs.dfs('A')

print("\nBFS:")
g_bfs = GraphBFS()
g_bfs.graph = g.graph
g_bfs.bfs('A')

# Shortest Path using Dijkstra
g_dijkstra = GraphDijkstra()
g_dijkstra.graph = g.graph
distances = g_dijkstra.dijkstra('A')
print("\nDijkstra's shortest path distances:", distances)

# Shortest Path using Bellman-Ford
g_bellman_ford = GraphBellmanFord()
g_bellman_ford.graph = g.graph
distances = g_bellman_ford.bellman_ford('A')
print("Bellman-Ford shortest path distances:", distances)
```

