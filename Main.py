#Import tkinter library
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from functools import partial
from Assets.uninformedSearch import *
from Assets.informedSearch import *

#Create an instance of tkinter frame or window
window= Tk()
window.resizable(0,0)

#Define a function to Opening the specific file using filedialog
def open_file():
    
    main = Main(window)
    
    for widgets in main.mainframe.winfo_children():
        widgets.destroy()
    
    path= filedialog.askopenfilename(title="Select a file", filetypes=(("text files","*.txt"),
    ("all files","*.*")))

    file= open(path,'r')
    txt= file.read().splitlines()
    
    rows, cols = (int(txt[0])+2, int(txt[1]))
    
    for i in range(2,rows):
        col = []
        for j in range(cols):
            if(txt[i].split()[j]=="W"):
                col.append("#")
            elif(txt[i].split()[j]=="D"):
                col.append(" ")
        main.maze.append(col)
    file.close()

    label.destroy()
    button.destroy()
    main.draw()

class Main():
    
    def __init__(self, win):
        self.win = win
        self.mainframe=Frame(self.win)
        self.mainframe.pack(fill="none",expand=True)
        self.maze = []
        self.path = []
        
    def draw(self):
        
        grid_frame=Frame(self.mainframe,bg="black")
        
        for row in range(0,len(self.maze)):
            for column in range(0,len(self.maze[0])):
                if(self.maze[row][column]==" "):
                    label1=Label(grid_frame,text="D",bg="#E0E0E0",fg="black",padx=2,pady=2)
                elif(self.maze[row][column]=="#"):
                    label1=Label(grid_frame,text="W",bg="#039BE5",fg="black",padx=2,pady=2)
                label1.grid(row=row,column=column,padx=0.5,pady=0.5,sticky="nsew")
                grid_frame.grid_columnconfigure(column,weight=1)
        
        DFSbtn=ttk.Button(self.mainframe, text="Depth First Search", command=self.dfsrun)
        DFSbtn.pack()
        
        BFSbtn=ttk.Button(self.mainframe, text="Breadth First Search",command=self.bfsrun)
        BFSbtn.pack()
        
        bestsearchbtn=ttk.Button(self.mainframe, text="Best First Search",command=self.bestfirstrun)
        bestsearchbtn.pack()
        
        astarbtn=ttk.Button(self.mainframe, text="A* Search",command=self.astarrun)
        astarbtn.pack()
        
        self.win.geometry("750x450")
        grid_frame.pack(fill="x")

    def dfsrun(self):
        
        uninformeds = uninformed_search(self.maze)
        
        self.path = uninformeds.DFS()
        if not(self.path==None):
            self.draw_path()
        else:
            self.draw_no_path()
    
    def bfsrun(self):
        
        uninformeds = uninformed_search(self.maze)
        
        self.path = uninformeds.BFS()
        if not(self.path==None):
            self.draw_path()
        else:
            self.draw_no_path()
    
    def bestfirstrun(self):
        
        informeds = informed_search(self.maze)
        
        self.path = informeds.best_first_search()
        if not(self.path==None):
            self.draw_path()
        else:
            self.draw_no_path()
    
    def astarrun(self):
        
        informeds = informed_search(self.maze)
        
        self.path = informeds.astar_search()
        if not(self.path==None):
            self.draw_path()
        else:
            self.draw_no_path()
    
    def draw_no_path(self):
        for widgets in window.winfo_children():
            widgets.destroy()
        
        self.mainframe=Frame(window)
        self.mainframe.pack(fill="none",expand=True)
        label= Label(self.mainframe,text = "Path Not Found\n\nPlease Select .txt file with following format\n4\n7\nW W W W D D D\nD D W D W D W\nW W D D W W D\nD W W W W D W\nwhere 4 and 7 = width and height\nW is Water and D is Dry Land", 
            font=('Courier 13'))
        label.pack()
        button=ttk.Button(self.mainframe, text="Open",command=open_file)
        button.pack()
    
    def draw_path(self):
        for widgets in window.winfo_children():
            widgets.destroy()
        
        self.mainframe=Frame(window)
        self.mainframe.pack(fill="none",expand=True)
        grid_frame=Frame(self.mainframe,bg="black")
        
        for row in range(0,len(self.path)):
            for column in range(0,len(self.path[0])):
                if(self.path[row][column]==" "):
                    label1=Label(grid_frame,text="D",bg="#E0E0E0",fg="black",padx=2,pady=2)
                elif(self.path[row][column]=="#"):
                    label1=Label(grid_frame,text="W",bg="#039BE5",fg="black",padx=2,pady=2)
                elif(self.path[row][column]=="+"):
                    label1=Label(grid_frame,text=">",bg="#76FF03",fg="black",padx=2,pady=2)
                label1.grid(row=row,column=column,padx=0.5,pady=0.5,sticky="nsew")
                grid_frame.grid_columnconfigure(column,weight=1)
        
        grid_frame.pack(fill="x")


#Create a button for opening files
label= Label(window,text = "Please Select .txt file with following format\n4\n7\nW W W W D D D\nD D W D W D W\nW W D D W W D\nD W W W W D W\nwhere 4 and 7 = width and height\nW is Water and D is Dry Land", 
            font=('Courier 13'))
label.pack()
button=ttk.Button(window, text="Open",command=open_file)
button.pack()
window.mainloop()