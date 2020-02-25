from tkinter import *

root = Tk()

with open("biodata.txt", "r") as f:
    Label(root, text=f.read(), width="40", height="10", justify="left").pack()

root.mainloop()