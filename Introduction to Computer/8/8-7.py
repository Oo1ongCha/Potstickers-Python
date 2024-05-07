from tkinter import*
tk=Tk()
cvs=Canvas(tk,width=400,height=400)
cvs.pack()
item1=cvs.create_polygon(10,10,10,60,50,35)

def movepolygon(event):
    if event.keysym=="Up":
        cvs.move(item1,0,-6)
    elif event.keysym=="Down":
        cvs.move(item1,0,6)
    elif event.keysym=="Left":
        cvs.move(item1,-6,0)
    else:
        cvs.move(item1,6,0)

cvs.bind_all("<KeyPress-Up>",movepolygon)
cvs.bind_all("<KeyPress-Down>",movepolygon)
cvs.bind_all("<KeyPress-Left>",movepolygon)
cvs.bind_all("<KeyPress-Right>",movepolygon)
