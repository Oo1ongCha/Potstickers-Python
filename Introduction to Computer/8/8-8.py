from tkinter import*

tk=Tk()
cvs=Canvas(tk,width=600,height=600,bg="red")
cvs.pack()

k=10

for i in range(0,26):
    cvs.create_oval(300+k,300+k,300-k,300-k,width=1)
    k=k+10
