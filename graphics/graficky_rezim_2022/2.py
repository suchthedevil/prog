import tkinter
import random

canvas = tkinter.Canvas(width=900,height=600, bg="navy")
canvas.pack()

n = 100
for i in range(n):
    x, y = random.randrange(10,890), random.randrange(10,590)
    canvas.create_text(x,y, font="arial 20", text="*", fill="yellow")


canvas.mainloop()
