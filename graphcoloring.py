class Graph:
    def __init__(self, vertices):
        # Initialize the number of vertices in the graph and create an adjacency list representation
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        # Add edges between vertices 'u' and 'v' by appending 'v' to the adjacency list of 'u' and vice versa
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_safe(self, v, c, color):
        # Check if it's safe to assign color 'c' to vertex 'v' based on its neighboring vertices' colors
        for i in self.graph[v]:
            if color[i] == c:
                return False
        return True

    def graph_color_util(self, m, color, v):
        # A utility function to recursively assign colors to vertices
        if v == self.V:
            return True
        # Try all colors from 1 to m for vertex 'v'
        for c in range(1, m+1):
            # Check if assigning color 'c' to vertex 'v' is safe
            if self.is_safe(v, c, color):
                color[v] = c
                # Recur for the next vertex
                if self.graph_color_util(m, color, v+1):
                    return True
                # If assigning color 'c' doesn't lead to a solution, backtrack
                color[v] = 0
        return False

    def graph_color(self, m):
        # Initialize an array to store colors assigned to vertices (0 represents unassigned)
        color = [0] * self.V
        # Call the utility function to assign colors to vertices
        if not self.graph_color_util(m, color, 0):
            # If no solution is found, print a message
            print("Solution does not exist")
            return False
        # If a solution is found, print the colors assigned to each vertex
        for i in range(self.V):
            print("Vertex", i, ":", "Color", color[i])
        return True

# Create a graph with 5 vertices
g = Graph(5)
# Add edges to the graph
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)
# Color the graph using 3 colors
g.graph_color(3)
