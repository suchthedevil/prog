import tkinter

canvas = tkinter.Canvas(width=900,height=600)
canvas.pack()

def rgb_color(rgb):
    return '#%02x%02x%02x' % rgb

x,y = 425, 100
n = 8

g = 255

for i in range(1,n+1):
    canvas.create_rectangle(x-25*i,y+50*i, x+25*i,y+50*(i+1),
    fill=rgb_color((0, g, 0)))
    g -= 30

canvas.mainloop()
