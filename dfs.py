# Define the graph as a dictionary where each key represents a node
# and its corresponding value is a list of its neighbors
graph = {
  '5' : ['3', '7'],   # Node '5' has neighbors '3' and '7'
  '3' : ['2', '4'],   # Node '3' has neighbors '2' and '4'
  '7' : ['8'],        # Node '7' has neighbor '8'
  '4' : ['8'],        # Node '4' has neighbor '8'
  '2' : [],           # Node '2' has no neighbors
  '8' : []            # Node '8' has no neighbors
}

# Initialize an empty set to keep track of visited nodes
visited = set()

# Define the depth-first search function
def dfs(visited, graph, node):
  # Check if the current node has not been visited yet
  if node not in visited:
    # Print the current node
    print(node)
    # Add the current node to the set of visited nodes
    visited.add(node)
    # For each neighbor of the current node
    for neighbour in graph[node]:
      # Recursively call the dfs function for unvisited neighbors
      dfs(visited, graph, neighbour)

# Main program starts here
print("The dfs is :")  # Print a message indicating the start of depth-first search
# Call the dfs function with the starting node '5'
dfs(visited, graph, '5')
