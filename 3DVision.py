from tkinter import *
import  math
from PIL import Image, ImageTk

# class Main (Frame):
#     def __init__(self, root):
#         super().__init__(root)

def btnBall_Click(event):
    global figure
    figure = Ball(300)
    print(figure)
    Print()

def MouseLeft(event):
    global lbDebug
    lbDebug.config(text = 'Левая кнопка мыши')      
 
def MouseRight(event):
    global lbDebug
    lbDebug.config(text = 'Правая кнопка мыши')    

def MouseMove(event):
    global lbDebug
    # if event.find('Button1') != -1:
    #     lbDebug.config(text = 'Правая кнопка мыши')   
    print(event)
    x = event.x
    y = event.y
    s = "Движение мышью {}x{}".format(x, y)

    lbDebug.config(text = s)

# =========== Figure ===========
def Ball(R):
    listpoint = []
    pi = math.pi
    i = 0
    while i < 2:
        j = 0
        z = R * math.cos(pi * i)
        while j < 2:
            x = R * math.sin(pi * i) * math.cos(pi * j)
            y = R * math.sin(pi * i) * math.sin(pi * j)
            point3D = {'x': 0, 'y': 0, 'z': 0}
            point3D['x'] = x
            point3D['y'] = y
            point3D['z'] = z
            listpoint.append(point3D)
            j = j + 0.1
        i = i + 0.1
            
    return listpoint

def Cube(Width):
    listpoint = [
        {'x': 0, 'y': 0, 'z': 0},
        {'x': 0, 'y': 0, 'z': 0},
        {'x': 0, 'y': 0, 'z': 0},
        {'x': 0, 'y': 0, 'z': 0},
        {'x': 0, 'y': 0, 'z': 0},
        {'x': 0, 'y': 0, 'z': 0},
        {'x': 0, 'y': 0, 'z': 0},
        {'x': 0, 'y': 0, 'z': 0},
        {'x': 0, 'y': 0, 'z': 0},
        {'x': 0, 'y': 0, 'z': 0},
        {'x': 0, 'y': 0, 'z': 0}
    ]
    return listpoint

def Print ():
    global figure, cavans

    i = -1
    for point1 in figure:
        point0 = figure[i]
        i = i + 1

        x0 = point0['x'] + 500 / 2
        y0 = point0['y'] + 500 / 2

        x1 = point1['x'] + 500 / 2
        y1 = point1['y'] + 500 / 2

        cavans.create_line(x0, y0, x1, y1)

if __name__ == "__main__":
    root = Tk()
    figure = []

    # =========== Form ===========
    root.iconbitmap('sours/3d-model.ico')
    root.title('3DVision')

    # =========== Button ===========
    btnBall = Button(text = "Шар")
    btnBall.grid(row = 0, column = 0)

    btnCube = Button(text = "Куб")
    btnCube.grid(row = 0, column = 1)

    btnPrizm = Button(text = "Призма")
    btnPrizm.grid(row = 0, column = 2)

    # =========== Canvas ===========
    cavans = Canvas(root, width=500, height=500, bg='white')
    cavans.grid(row = 1, column = 0, columnspan = 3)

    # =========== Label ===========
    lbDebug = Label(text = '')
    lbDebug.grid(row = 2,  column = 0, columnspan = 3)                
 
    # =========== Bind ===========
    cavans.bind('<Button-1>', MouseLeft)
    cavans.bind('<Button-3>', MouseRight)
    cavans.bind('<Motion>', MouseMove)

    btnBall.bind('<Button-1>', btnBall_Click)
    
    root.mainloop()

