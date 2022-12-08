import tkinter, random

canvas = tkinter.Canvas(width=1000, height=600)
canvas.pack()

n = 20
r = 30

for i in range(1,n+1):
    x, y = random.randrange(30,970), random.randrange(30,570) 
    canvas.create_oval(x-r,y-r,x+r,y+r, fill="yellow", tags=f"c{i}")
    canvas.create_text(x,y, text=i, font="Arial 20", tags=f"c{i}" )

for i in range(100000000):
    for j in range(n):
        x, y = random.randrange(-3,4), random.randrange(-3,4)
        canvas.move(f"c{j+1}", x, y)
    canvas.after(50)
    canvas.update()

tkinter.mainloop()
