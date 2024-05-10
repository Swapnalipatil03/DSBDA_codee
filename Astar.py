import heapq

class Node:
    def __init__(self, x, y, cost, parent=None):
        # Initialize the attributes of the node
        self.x = x  # x-coordinate of the node in the grid
        self.y = y  # y-coordinate of the node in the grid
        self.cost = cost  # Cost of moving to this node
        self.parent = parent  # Parent node in the path
        self.g = 0  # Actual cost from the start node to this node
        self.h = 0  # Heuristic cost from this node to the goal node
        self.f = 0  # Total cost (g + h) for this node

    def __lt__(self, other):
        # Define comparison method for nodes, used by heapq
        return self.f < other.f

def heuristic(node, goal):
    # Calculate the Manhattan distance heuristic between two nodes
    return abs(node.x - goal.x) + abs(node.y - goal.y)

def a_star_search(start, goal, grid):
    # Create the start and goal nodes
    start_node = Node(start[0], start[1], grid[start[0]][start[1]])
    goal_node = Node(goal[0], goal[1], grid[goal[0]][goal[1]])

    open_list = []  # Priority queue to store nodes to be explored
    closed_list = set()  # Set to store nodes that have been explored

    heapq.heappush(open_list, start_node)  # Add the start node to the open list

    while open_list:
        current_node = heapq.heappop(open_list)  # Get the node with the lowest f value from the open list

        if current_node.x == goal_node.x and current_node.y == goal_node.y:
            # If the current node is the goal node, construct and return the path
            path = []
            while current_node is not None:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            return path[::-1]  # Reverse the path to get it from start to goal

        closed_list.add((current_node.x, current_node.y))  # Add the current node to the closed list

        # Generate neighboring nodes
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor_x = current_node.x + x
            neighbor_y = current_node.y + y

            # Check if the neighbor is within the grid boundaries
            if neighbor_x < 0 or neighbor_x >= len(grid) or neighbor_y < 0 or neighbor_y >= len(grid[0]):
                continue

            # Check if the neighbor is an obstacle or already explored
            if grid[neighbor_x][neighbor_y] == -1 or (neighbor_x, neighbor_y) in closed_list:
                continue

            # Create the neighbor node
            neighbor_node = Node(neighbor_x, neighbor_y, grid[neighbor_x][neighbor_y], current_node)

            # Calculate the cost values for the neighbor node
            neighbor_node.g = current_node.g + neighbor_node.cost
            neighbor_node.h = heuristic(neighbor_node, goal_node)
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            # Add the neighbor node to the open list
            heapq.heappush(open_list, neighbor_node)

    return None  # Return None if no path is found

# Define the start and goal points, and the grid with costs
start = (0, 0)
goal = (3, 3)
grid = [[0, 1, 2, 3],
        [1, 2, -1, 4],
        [2, -1, 4, 5],
        [3, 4, 5, 6]]

# Perform A* search to find the path
path = a_star_search(start, goal, grid)
print(path)  # Print the resulting path
