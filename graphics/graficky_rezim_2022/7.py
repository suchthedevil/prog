import tkinter

canvas = tkinter.Canvas()
canvas.pack()

n = 16

x, y = 10, 100
d = 20
for i in range(n):
    x1, y1 = x+abs(d), y+d
    canvas.create_line(x, y, x1, y1,)
    x, y = x1, y1
    d = -d

tkinter.mainloop()