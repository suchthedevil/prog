import tkinter
import random

canvas = tkinter.Canvas(width=900,height=600)
canvas.pack()
n = 15
x, y = 140,20
f1, f2, f3 = 'red', 'blue', 'yellow' 

for i in reversed(range(10,n*10,10)):
    canvas.create_rectangle(x,y, x+i,y+i, fill=f1)
    x+=5
    y+=5
    f1, f2, f3 = f3, f1, f2

canvas.mainloop()
