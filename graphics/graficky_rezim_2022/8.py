import tkinter

canvas = tkinter.Canvas(height=500, width=800)
canvas.pack()

x, y = 70, 100
r = 50
dx, dy = 120, 60
colors = ["blue", "yellow", "black", "green", "red"]

for c in colors:
    canvas.create_oval(x-r,y-r,x+r,y+r, width=15, outline=c)
    x += dx/2
    dy = -dy
    y -= dy

tkinter.mainloop()
