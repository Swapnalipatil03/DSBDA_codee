# Define the number of nodes
N = 5

# Define a large value representing infinity
INF = 99999999

# Initialize an array to keep track of selected nodes
selected_node = [0,0,0,0,0]

# Define the graph as an adjacency matrix
G = [[0, 19, 5, 0, 0],
     [19, 0, 5, 9, 2],
     [5, 5, 0, 1, 6],
     [0, 9, 1, 0, 1],
     [0, 2, 6, 1, 0]]

# Start with the first node selected
selected_node[0] = True

# Initialize the number of edges
no_edge = 0

# Print a header for the output
print("Edge : Weight \n")

# Loop until all nodes are selected
while(no_edge < N-1):
    # Initialize the minimum weight to infinity
    minimum = INF
    # Initialize variables to store the indices of nodes forming the minimum weight edge
    a = 0
    b = 0
    # Iterate through all nodes
    for m in range(N):
        # Check if the node m is selected
        if selected_node[m]:
            # Iterate through all nodes
            for n in range(N):
                # Check if the node n is not selected and there is an edge between m and n
                if ((not selected_node[n]) and G[m][n]):
                    # If the weight of the edge between m and n is smaller than the current minimum weight
                    if minimum > G[m][n]:
                        # Update the minimum weight and the indices of nodes forming the minimum weight edge
                        minimum = G[m][n]
                        a = m
                        b = n
    # Print the selected edge and its weight
    print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
    # Mark node b as selected
    selected_node[b] = True
    # Increment the number of edges selected
    no_edge += 1
