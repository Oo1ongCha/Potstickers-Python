from tkinter import*

tk1=Tk()
tk1.title("a line")
evs1= Canvas(tk1,width=200,height=200)
cvs1.pack()
cvs1.create_line(0,0,200,200,width=2,fill="green")

tk2=Tk()
tk2.title("two rectangles")
evs2= Canvas(tk2,width=400,height=400)
cvs2.pack()
cvs2.create_rectangle(10,10,300,50,outline="red")
cvs2.create_rectangle(10,10,50,300,outline="blue")
