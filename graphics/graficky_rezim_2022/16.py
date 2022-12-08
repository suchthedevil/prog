import tkinter

canvas = tkinter.Canvas(height=500, width=800)
canvas.pack()

row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
vel = 30
farba1, farba2 = 'maroon', 'gold'

x, y = 10, 10

tkinter.mainloop()