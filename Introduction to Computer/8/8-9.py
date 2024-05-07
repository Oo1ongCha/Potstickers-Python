from tkinter import*

tk=Tk()
cvs=Canvas(tk,width=600,height=600,bg="yellow")
cvs.pack()

k=10

for i in range(0,26):
    cvs.create_rectangle(400+k,400+k,400-k,400-k,width=1)
    k=k+10
