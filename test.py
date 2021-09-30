import queue

def createMaze():

    maze = []

    maze.append(["#","#", "#", "#", "#", "#", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", "#", " ", "#", "#", " ", " "])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append([" "," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", "#", " "])
    maze.append([" "," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#","#", "#", "#", "#", "#", "#", "#", "#"])

    return maze

def printMaze(maze, row, path=""):

    start = row

    i = start
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

def DFS(maze):
    start = []
    
    for row in range(0,len(maze)):
        if maze[row][0] == " ":
            start.append(row)
    
    row = start.pop(0)
    
    explored=[]
    frontier=[]
    
    explored.append(str(row))
    frontier.append("")
    dfsPath=""
    
    while len(frontier)>0 :
        
        currCell=frontier.pop()
        
        if findEnd(maze, row, dfsPath):
            break
        
        for d in 'RUD':
            childCell = currCell + d
            if valid(maze, row, childCell):
                if childCell in explored:
                    continue
                explored.append(childCell)
                frontier.append(childCell)
                dfsPath=currCell
        
        if len(frontier)==1 and not findEnd(maze, row, dfsPath) and start.__len__() >0:
            explored =[]
            frontier =[]
            dfsPath=""
            row = start.pop(0)
            explored.append(str(row))
            frontier.append("")


def BFS(maze):
    start = []
    
    for row in range(0,len(maze)):
        if maze[row][0] == " ":
            start.append(row)
    
    row = start.pop(0)
    
    explored=[]
    frontier=[]
    
    explored.append(str(row))
    frontier.append("")
    bfsPath=""
    
    while len(frontier)>0 :
        
        currCell=frontier.pop(0)
        
        if findEnd(maze, row, bfsPath):
            break
        
        for d in 'RUD':
            childCell = currCell + d
            if valid(maze, row, childCell):
                if childCell in explored:
                    continue
                explored.append(childCell)
                frontier.append(childCell)
                bfsPath=currCell
        
        if len(frontier)==1 and not findEnd(maze, row, bfsPath) and start.__len__() >0:
            explored =[]
            frontier =[]
            bfsPath=""
            row = start.pop(0)
            explored.append(str(row))
            frontier.append("")
# MAIN ALGORITHM

maze  = createMaze()
DFS(maze)
BFS(maze)