import queue

def createMaze():

    maze = []

    #"DRUURR"
    maze.append(["#","#", "#", "#", "#", "#","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append([" "," ", "#", " ", "#", " "," "])
    maze.append(["#"," ", "#", " ", " ", " ","#"])
    maze.append(["#"," ", "#", "#", "#", " "," "])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#","#", "#", "#", "#", "#","#"])

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

        elif move == "D" :
            j += 1
            i += 1
            
    if j == maze[0].__len__()-1:
        print("Found: " + moves)
        printMaze(maze, row, moves)
        return True
    return False

# MAIN ALGORITHM

nums = []
nums.append("")
add = ""
maze  = createMaze()
start = queue.Queue()

for row in range(0,maze.__len__()):
    if maze[row][0] == " ":
        start.put(row)

row = start.get()

while not findEnd(maze, row, add) and start.not_empty: 
    if nums.__len__()==0:
        nums.append("")
        add = ""
        row = start.get()

    add = nums.pop()
    #print(add)
    print("row :" + str(row+1))
    for j in ["R", "U", "D"]:
        put = add + j
        print("Added Path :" + put)
        if valid(maze, row, put) and not(put.__len__() == maze[0].__len__()):
            nums.append(put)
        else:
            break