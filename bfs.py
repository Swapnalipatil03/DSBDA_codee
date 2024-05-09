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

# Initialize an empty list to keep track of visited nodes during BFS
visited = []

# Initialize an empty queue for BFS traversal
queue = []

# Define the breadth-first search (BFS) function
def bfs(visited, graph, node):
  # Mark the current node as visited and enqueue it
  visited.append(node)
  queue.append(node)
  # Loop until the queue is empty
  while queue:
    # Dequeue a node from the queue
    m = queue.pop(0)
    # Print the dequeued node
    print(m, end=" ")
    # Visit and enqueue all the neighbors of the dequeued node
    for neighbour in graph[m]:
      # If a neighbor has not been visited yet
      if neighbour not in visited:
        # Mark it as visited and enqueue it
        visited.append(neighbour) 
        queue.append(neighbour)

# Main program starts here
print("The bfs is: ")  # Print a message indicating the start of BFS traversal
# Call the BFS function with the starting node '5'
bfs(visited, graph, '5')
