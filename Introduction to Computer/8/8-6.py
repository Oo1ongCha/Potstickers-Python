from tkinter import*
from time import*

tk=Tk()
cvs=Canvas(tk,width=400,height=300)
cvs.pack()
item1=cvs.create_polygon(10,10,60,50,35)
item1=cvs.create_polygon(350,200,350,250,310,225)

for i in range (60):
    cvs.move(item1,5,0)
    tk.update()
    sleep(0.05)

for i in range (60):
    cvs.move(item2,-5,0)
    tk.update()
    sleep(0.05)
    
