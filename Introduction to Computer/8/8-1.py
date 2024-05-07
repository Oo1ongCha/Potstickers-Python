from tkinter import*

tk1=Tk()
btn1=Button(tk1,text="click here")
btn1.pack()

btn2=Button(tk1,text="another button")
btn2.pack()

def sayhello():
    print ("Hello, how R you today ?")

tk2=Tk()
btn3=Button (tk2, text="click and see",command =sayhello)
btn3.pack()
