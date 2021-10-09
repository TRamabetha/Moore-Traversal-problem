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

# Check if a neighbor should be added to open list
def add_to_open(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f >= node.f):
            return False
    return True

def createMaze():

    maze = []

    maze.append(["#","#", "#", "#", " ", " ", "#"])
    maze.append([" "," ", "#", " ", "#", " ", " "])
    maze.append(["#","#", " ", "#", "#", "#", "#"])
    maze.append([" ","#", "#", "#", " ", " ", "#"])
    maze.append(["#"," ", " ", " ", "#", "#", " "])
    
    return maze

def createMaze2():
    
    maze = []
    
    maze.append(["#","#", "#", "#", "#", "#", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append([" "," ", "#", "#", " ", "#", "#", " ", " "])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append([" "," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", "#", "#"])
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

def get_maze_arr(maze, row, path=""):
    arr = maze
    
    i = row
    j = 0

    arr[i][j]="+"
    
    for move in path:

        if move == "R":
            j += 1

        elif move == "U":
            j += 1
            i -= 1

        elif move == "D":
            j += 1
            i += 1
            
        arr[i][j]="+"

    return arr

def valid(maze, row, moves):

    i = row
    j = 0

    for move in moves:

        if move == "R":
            j += 1

        elif move == "U":
            j += 1
            i -= 1

        elif move == "D":
            j += 1
            i += 1

        if (j > len(maze[0]) or i > len(maze)) or (j < 0 or i < 0):
            return False
        
        if(j == len(maze[0]) or i == len(maze)):
            if (maze[i-1][j-1] == "#"):
                return False
        else:
            if (maze[i][j] == "#"):
                return False
    return True

def is_informed_valid(maze, position:()):

    (i,j)= position
    
    if (j > len(maze[0]) or i > len(maze)) or (j < 0 or i < 0):
        return False
    
    if(j == len(maze[0]) or i == len(maze)):
        if (maze[i-1][j-1] == "#"):
            return False
    else:
        if (maze[i][j] == "#"):
            return False
    
    return True


def findEnd(maze,row, moves):
    
    if moves == "":
        return False
    
    i = row
    j = 0
    
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
        return True
    return False
