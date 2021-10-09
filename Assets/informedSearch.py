from Assets.algoAssets import *

class informed_search:
    
    def __init__(self, maze):
        self.maze = maze
    
    # Best-first search
    def best_first_search(self):
        start = []
        goal = []
        
        for row in range(0,len(self.maze)):
            if self.maze[row][0] == " ":
                start.append(row)
            if self.maze[row][len(self.maze)-1] == " ":
                goal.append(Node((row,len(self.maze)), None,""))
                
        
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
            
            # Check if we have reached the goal, return the path
            (row, col) = start_node.position
            if findEnd(self.maze, row, current_node.path):
                arr = get_maze_arr(self.maze, row, current_node.path)
                return arr
            
            # Unzip the current node position
            (x, y) = current_node.position
            
            # Loop neighbors
            for d in 'RUD':
                nextpath=current_node.path+d
                
                # Check if the node is a wall
                if not valid(self.maze, row, nextpath):
                    continue
                
                if d == "R":
                    next= (x+1, y)
                if d == "U":
                    next= (x-1, y+1)
                if d == "D":
                    next= (x+1, y+1)
                
                # Create a neighbor node
                neighbor = Node(next, current_node,nextpath)
                
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
            
            # Add the current node to the closed list
            closed.append(current_node)
            
            if len(open)==0 and not findEnd(self.maze, row, current_node.path) and start.__len__() >0:
                start_node = Node((start.pop(0),0), None,"")
                open = []
                closed = []
                open.append(start_node)
        # Return None, no path is found
        return None

    # A* search
    def astar_search(self):
        start = []
        goal = []
        
        for row in range(0,len(self.maze)):
            if self.maze[row][0] == " ":
                start.append(row)
            if self.maze[row][len(self.maze)-1] == " ":
                goal.append(Node((row,len(self.maze)), None,""))
        
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
            if findEnd(self.maze, row, current_node.path):
                arr = get_maze_arr(self.maze, row, current_node.path)
                return arr
            
            # Unzip the current node position
            (x, y) = current_node.position
            # Get neighbors
            
            # Loop neighbors
            for d in 'RUD':
                nextpath=current_node.path+d
                
                # Check if the node is a wall
                if not valid(self.maze, row, nextpath):
                    continue
                
                if d == "R":
                    next= (x+1, y)
                if d == "U":
                    next= (x-1, y+1)
                if d == "D":
                    next= (x+1, y+1)
                
                # Create a neighbor node
                neighbor = Node(next, current_node,nextpath)
                
                # Generate heuristics (Manhattan distance)
                neighbor.g = abs(neighbor.position[0] - start_node.position[0]) + abs(neighbor.position[1] - start_node.position[1])
                temp = abs(neighbor.position[0] - goal_node.position[0]) + abs(neighbor.position[1] - goal_node.position[1])
                for end in goal:
                    if temp > abs(neighbor.position[0] - end.position[0]) + abs(neighbor.position[1] - end.position[1]):
                        temp= abs(neighbor.position[0] - end.position[0]) + abs(neighbor.position[1] - end.position[1])
                neighbor.h = temp
                neighbor.f = neighbor.g + neighbor.h
                # Check if neighbor is in open list and if it has a lower f value
                if(add_to_open(open, neighbor) == True):
                    # Everything is green, add neighbor to open list
                    open.append(neighbor)
            
            if len(open)==0 and not findEnd(self.maze, row, current_node.path) and start.__len__() >0:
                start_node = Node((start.pop(0),0), None,"")
                open = []
                closed = []
                open.append(start_node)
        # Return None, no path is found
        return None

