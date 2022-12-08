import tkinter

canvas = tkinter.Canvas(width=800,height=800)
canvas.pack()

x, y = 400, 400 
r = 300
for i in range(10):
    id = canvas.create_oval(x-r,y-r,x+r,y+r, tags="k"+str(i))
    r -= 30
    print(id)

    canvas.after(200)
    canvas.update()

canvas.delete(3)
canvas.move(4,50,-50)

canvas.itemconfig("k5", outline="red", width=4)

canvas.coords(5, 200, 400, 200, 400)

tkinter.mainloop()