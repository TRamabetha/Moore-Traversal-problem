# This class represents a node
class Node:
    # Initialize the class
    def __init__(self, position:(), parent:(), path = str):
        self.position = position
        self.parent = parent
        self.path = path
        self.g = 0 # Distance to start node
        self.h = 0 # Distance to goal node
        self.f = 0 # Total cost
    # Compare nodes
    def __eq__(self, other):
        return self.position == other.position
    # Sort nodes
    def __lt__(self, other):
        return self.f < other.f
    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))

def createMaze():

    maze = []

    maze.append(["#","#", "#", "#", "#", "#", "#", "#", "#"])
    maze.append(["#"," ", "#", "#", " ", "#", "#", " ", " "])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append([" "," ", " ", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", "#", " "])
    maze.append([" "," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#","#", "#", "#", "#", "#", "#", "#", "#"])

    return maze

def printMaze(maze, row, path=""):

    i = row
    j = 0

    pos = set()
    pos.add((i, j))

    for move in path:

        if move == "R":
            j += 1

        elif move == "U":
            j += 1
            i -= 1

        elif move == "D":
            j += 1
            i += 1
            
        pos.add((i, j))

    for i, row in enumerate(maze):

        for j, col in enumerate(row):

            if (i, j) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")

        print()

    return True


def valid(maze, row, moves):

    i = row
    j = 0

    for move in moves:

        if move == "R"and not(j == maze[0].__len__()-1):
            j += 1

        elif move == "U" and not(j == maze[0].__len__()-1):
            j += 1
            i -= 1

        elif move == "D" and (i < maze.__len__() -1 or j == maze[0].__len__() -1):
            j += 1
            i += 1

        if not(0 <= j < len(maze[0]) and 0 <= i <= len(maze)):
            return False

        elif (maze[i][j] == "#"):
            return False
        
    return True


def findEnd(maze,row, moves):
    
    if moves == "":
        return False
    
    print("test :" + moves)
    
    i = row
    j = 0
    if not valid(maze, row, moves):
        return False
    for move in moves:
        
        if move == "R":
            j += 1

        elif move == "U":
            j += 1
            i -= 1

        elif move == "D" and i < maze.__len__() -1 :
            j += 1
            i += 1
    
    if j == maze[0].__len__()-1:
        print("Found: " + moves)
        printMaze(maze, row, moves)
        return True
    return False

# Best-first search
def best_first_search(maze):
    start = []
    goal = []
    
    for row in range(0,len(maze)):
        if maze[row][0] == " ":
            start.append(row)
        if maze[row][len(maze)] == " ":
            goal.append(Node((row,len(maze)), None,""))
            
    
    # Create lists for open nodes and closed nodes
    open = []
    closed = []
    # Create a start node and an goal node
    start_node = Node((start.pop(0),0), None,"")
    goal_node = goal.pop(0)
    # Add the start node
    open.append(start_node)
    
    # Loop until the open list is empty
    while len(open) > 0:
        # Sort the open list to get the node with the lowest cost first
        open.sort()
        # Get the node with the lowest cost
        current_node = open.pop(0)
        # Add the current node to the closed list
        closed.append(current_node)
        
        # Check if we have reached the goal, return the path
        (row, col) = start_node.position
        if findEnd(maze, row, current_node.path):
            break
        
        # Unzip the current node position
        (x, y) = current_node.position
        # Get neighbors
        neighbors = [(x+1, y), (x+1, y+1), (x-1, y+1)]
        # Loop neighbors
        for next in neighbors:
            nextpath=current_node.path
            
            if next ==(x+1, y):
                nextpath+="R"
            elif next ==(x+1, y+1):
                nextpath+="D"
            elif next ==(x-1, y+1):
                nextpath+="U"
            
            # Check if the node is a wall
            if not valid(maze, row, nextpath):
                continue
            # Create a neighbor node
            neighbor = Node(next, current_node,nextpath)
            # Check if the neighbor is in the closed list
            if(neighbor in closed):
                continue
            # Generate heuristics (Manhattan distance)
            neighbor.g = abs(neighbor.position[0] - start_node.position[0]) + abs(neighbor.position[1] - start_node.position[1])
            temp = abs(neighbor.position[0] - goal_node.position[0]) + abs(neighbor.position[1] - goal_node.position[1])
            for end in goal:
                if temp > abs(neighbor.position[0] - end.position[0]) + abs(neighbor.position[1] - end.position[1]):
                    temp= abs(neighbor.position[0] - end.position[0]) + abs(neighbor.position[1] - end.position[1])
            neighbor.h = temp
            neighbor.f = neighbor.h
            # Check if neighbor is in open list and if it has a lower f value
            if(add_to_open(open, neighbor) == True):
                # Everything is green, add neighbor to open list
                open.append(neighbor)
            
        if len(open)==1 and not findEnd(maze, row, current_node.path) and start.__len__() >0:
            start_node = Node((start.pop(0),0), None,"")
            open = []
            closed = []
            open.append(start_node)
    # Return None, no path is found
    return None
# Check if a neighbor should be added to open list
def add_to_open(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f >= node.f):
            return False
    return True


# MAIN ALGORITHM

maze  = createMaze()
best_first_search(maze)