class Graph:
    def __init__(self,vertices):
        # Initialize the number of vertices in the graph and an empty list to store edges
        self.V = vertices
        self.graph = []
  
    def add_edge(self,u,v,w):
        # Add an edge to the graph as a triplet (u, v, w) where 'u' and 'v' are vertices and 'w' is the weight of the edge
        self.graph.append([u,v,w])

    def find(self,parent, i):
        # Find operation for disjoint set, finds the root of the set containing element 'i'
        if(parent[i]==i):
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        # Union operation for disjoint set, merges two sets represented by 'x' and 'y'
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if (rank[xroot] < rank[yroot]):
            parent[xroot] = yroot
        elif (rank[xroot] > rank[yroot]):
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
  
    def kruskal_algo(self):
        # Initialize variables for edge and result count
        i, e = 0, 0
        result = []  # List to store the edges of the minimum spanning tree
        parent = []  # List to store the parent of each vertex in the disjoint set
        rank = []    # List to store the rank of each element in the disjoint set
        # Sort the edges of the graph based on their weights
        self.graph = sorted(self.graph, key = lambda item:item[2])
        # Initialize parent and rank arrays for disjoint set
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Iterate over all edges in the sorted order
        while e < self.V - 1:
            # Get the edge (u, v, w)
            u,v,w = self.graph[i]
            i = i+1
            # Find the root nodes of the sets containing 'u' and 'v'
            x = self.find(parent, u)
            y = self.find(parent, v)

            # If adding the edge (u, v) doesn't form a cycle, include it in the minimum spanning tree
            if x != y:
                e = e+1
                result.append([u,v,w])  # Add the edge to the result
                self.apply_union(parent, rank, x, y)  # Merge the sets containing 'u' and 'v'
      
        # Print the edges of the minimum spanning tree
        for u,v,w in result:
            print("%d - %d : %d" % (u,v,w))

# Create a graph with 6 vertices
g = Graph(6)
# Add edges to the graph
g.add_edge(0,1,4)  # 0 to 1, 4 weight is added
g.add_edge(0,2,4)
g.add_edge(1,2,2)
g.add_edge(1,0,4)
g.add_edge(2,0,4)
g.add_edge(2,1,2)
g.add_edge(2,3,3)
g.add_edge(2,5,2)
g.add_edge(2,4,4)
g.add_edge(3,2,3)
g.add_edge(3,4,3)
g.add_edge(4,2,4)
g.add_edge(4,3,3)
g.add_edge(5,2,2)
g.add_edge(5,4,3)

# Apply Kruskal's algorithm to find the minimum spanning tree and print the result
g.kruskal_algo()
