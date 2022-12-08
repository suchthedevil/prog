import tkinter

canvas = tkinter.Canvas(width=800,height=800,bg="cyan")
canvas.pack()

r1, r2, r3 = 20, 40, 60

x,y = 400,400

r = 20
for i in range(3):
    canvas.create_oval(x-r,y-r,x+r,y+r, fill="white")
    y += (2*r+20)
    r += 20
    canvas.after(500)
    canvas.update()



tkinter.mainloop()