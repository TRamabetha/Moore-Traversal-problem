#Import tkinter library
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
#Create an instance of tkinter frame or window
window= Tk()
window.geometry("750x150")
#Define a function to Opening the specific file using filedialog
def open_file():
    path= filedialog.askopenfilename(title="Select a file", filetypes=(("text files","*.txt"),
    ("all files","*.*")))

    file= open(path,'r')
    txt= file.read().splitlines()
    # for line in range(2,int(txt[0])+2):
    #     label= Label(window,text = txt[line], font=('Courier 13'))
    #     label.pack()
    rows, cols = (int(txt[0])+2, int(txt[1]))
    arr=[]
    for i in range(2,rows):
        col = []
        for j in range(cols):
            col.append(txt[i].split()[j])
        arr.append(col)
    label= Label(window,text = arr, font=('Courier 13'))
    label.pack()
    file.close()
    button.pack_forget()
    button.config(state=DISABLED)
    window.geometry("750x450")
    button.pack()
    
#Create a button for opening files
label= Label(window,text = "Please Select .txt file", font=('Courier 13'))
label.pack()
button=ttk.Button(window, text="Open",command=open_file)
button.pack()
window.mainloop()