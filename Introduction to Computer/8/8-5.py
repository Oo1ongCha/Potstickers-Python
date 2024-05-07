from tkinter import*

tk=Tk()
cvs=Canvas(tk,width=300,height=300)
cvs.pack()
cvs.create_polygon(10,10,100,10,100,110,
                   fill="green",outline="blue")
cvs.create_polygon(200,10,240,30,120,100,140,120,
                   fill="",outline="black")

cvs.create_text(150,150,text="Here are two polygons,")
cvs.create_text(150,200,text="with different type.",
                fill="red")
