from Assets.algoAssets import *

class uninformed_search:
    
    def __init__(self, maze):
        self.maze = maze
    
    def DFS(self):
        start = []
        
        for row in range(0,len(self.maze)):
            if self.maze[row][0] == " ":
                start.append(row)
        
        if start.__len__()>0:
            row = start.pop(0)
        else:
            return None
        
        explored=[]
        frontier=[]
        
        explored.append(str(row))
        frontier.append("")
        dfsPath=""
        
        while len(frontier)>0 :
            
            currCell=frontier.pop()
            
            if findEnd(self.maze, row, dfsPath):
                arr = get_maze_arr(self.maze, row, dfsPath)
                return arr
            
            for d in 'URD':
                childCell = currCell + d
                if valid(self.maze, row, childCell):
                    if childCell in explored:
                        continue
                    explored.append(childCell)
                    frontier.append(childCell)
                    dfsPath=currCell
            
            if len(frontier)==0 and not findEnd(self.maze, row, dfsPath) and start.__len__() >0:
                explored =[]
                frontier =[]
                dfsPath=""
                row = start.pop(0)
                explored.append(str(row))
                frontier.append("")
        return None

    def BFS(self):
        start = []
        
        for row in range(0,len(self.maze)):
            if self.maze[row][0] == " ":
                start.append(row)
        
        row = start.pop(0)
        
        explored=[]
        frontier=[]
        
        explored.append(str(row))
        frontier.append("")
        bfsPath=""
        
        while len(frontier)>0 :
            
            currCell=frontier.pop(0)
            
            if findEnd(self.maze, row, bfsPath):
                arr = get_maze_arr(self.maze, row, bfsPath)
                return arr
            
            for d in 'URD':
                childCell = currCell + d
                if valid(self.maze, row, childCell):
                    if childCell in explored:
                        continue
                    explored.append(childCell)
                    frontier.append(childCell)
                    bfsPath=currCell
            
            if len(frontier)==0 and not findEnd(self.maze, row, bfsPath) and start.__len__() >0:
                explored =[]
                frontier =[]
                bfsPath=""
                row = start.pop(0)
                explored.append(str(row))
                frontier.append("")
        return None
