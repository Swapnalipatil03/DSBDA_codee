import heapq

def dijkstras(graph, start, end):
    # Initialize a priority queue to store nodes to be visited
    pq = [(0, start, [start])]  # Tuple structure: (cost, current_node, path)
    # Initialize a set to keep track of visited nodes
    visited = set()
    
    # Iterate until the priority queue is empty
    while pq:
        # Pop the node with the lowest cost from the priority queue
        (cost, curr_node, path) = heapq.heappop(pq)
        
        # If the popped node is the destination node, return the path and cost
        if curr_node == end:
            return path, cost
        
        # If the current node has been visited, skip it
        if curr_node in visited:
            continue
        
        # Mark the current node as visited
        visited.add(curr_node)
        
        # Iterate over the neighbors of the current node
        for next_node, edge_cost in graph[curr_node]:
            # If the neighbor has not been visited, add it to the priority queue
            if next_node not in visited:
                # Add the neighbor node to the current path
                new_path = path + [next_node]
                # Calculate the new cost to reach the neighbor node
                new_cost = cost + edge_cost
                # Add the new cost and path to the priority queue
                heapq.heappush(pq, (new_cost, next_node, new_path))
    
    # If the destination node is not reachable, return None
    return None, float("inf")

# Define the graph as a dictionary with nodes as keys and lists of tuples (neighbor, edge_cost) as values
graph = {
    'A' : [('B', 5), ('C', 1)],
    'B' : [('A', 5), ('B', 2), ('D', 1)],
    'C' : [('A', 1), ('B', 2), ('D', 4)],
    'D' : [('B', 1), ('C', 4)]
}

# Call the Dijkstra's function to find the shortest path and distance between 'B' and 'D'
path, shortest_distance = dijkstras(graph, 'A', 'D')

# Print the shortest path and distance
if path:
    print("The shortest path from A to D is:", ' -> '.join(path))
    print("The total distance is:", shortest_distance)
else:
    print("There is no path from A to D")
