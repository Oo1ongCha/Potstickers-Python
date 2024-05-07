from tkinter import*
from random import*

tk=Tk()
cvs=Canvas(tk,width=400,height=400)
cvs.pack()

def random_rectangle(W,H,c):
    x1=randrange(W)
    y1=randrange(H)
    x2=x1+randrange(W)
    y2=y1+randrange(H)
    cvs.create_rectangle(x1,y1,x2,y2,fill=c)

Color=("green","red","blue","orange","yellow","pink","purple","violet","magenta","cyan")

L=len (Color)

for i in range (100):
    r=randrange(L)
    random_rectangle(200,200,Color[r])
