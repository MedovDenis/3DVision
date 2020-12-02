from tkinter import *
import math 
from PIL import Image, ImageTk

af = 0.1
bt = 0.1
gm = 0.1
k = 1.0
dx = 0
dy = 0
width = 500
height = 500

def btnUpRot_Click():
    global af
    af = af + 0.1
    # print(figure)
    Print()

def btnDownRot_Click():
    global af
    af = af - 0.1
    # print(figure)
    Print()

def btnRightRot_Click():
    global gm
    gm = gm + 0.1
    # print(figure)
    Print()

def btnLeftRot_Click():
    global gm
    gm = gm - 0.1
    # print(figure)
    Print()

def btnRightAround_Click():
    global bt
    bt = bt + 0.1
    # print(figure)
    Print()

def btnLeftAround_Click():
    global bt
    bt = bt - 0.1
    # print(figure)
    Print()

def btnHomeRot_Click():
    global af, bt, gm 
    af = 0
    bt = 0
    gm = 0
    Print()


def btnUp_Click():
    global dy
    dy = dy - 10
    # print(figure)
    Print()

def btnDown_Click():
    global dy
    dy = dy + 10
    # print(figure)
    Print()

def btnRight_Click():
    global dx
    dx = dx + 10
    # print(figure)
    Print()

def btnLeft_Click():
    global dx
    dx = dx - 10
    # print(figure)
    Print()

def btnZoomIncrease_Click():
    global k
    k = k + 0.1
    # print(figure)
    Print()

def btnZoomReduce_Click():
    global k
    k = k - 0.1
    # print(figure)
    Print()

def btnHome_Click():
    global dx, dy, k
    dx = 0
    dy = 0
    k = 1
    Print()


def btnBall_Click():
    global figure
    figure = Ball(100)
    # print(figure)
    Print()

def btnPear_Click():
    global figure
    figure = Pear(100)
    # print(figure)
    Print()

def btnTor_Click():
    global figure
    figure = Tor(100, 50)
    # print(figure)
    Print()

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
            j = j + 0.05
        i = i + 0.05
            
    return listpoint

def Pear(R):
    listpoint = []
    pi = math.pi
    i = 0
    while i < 2:
        j = 0
        if (R * math.cos(pi * i)) > R/2:
            z = R * math.cos(pi * i) + 2.5 * R *math.pow((R * math.cos(pi * i) / (R - 0.5)), 2)
        else:
            z = R * math.cos(pi * i)
        while j < 2:
            x = R * math.sin(pi * i) * math.cos(pi * j)
            y = R * math.sin(pi * i) * math.sin(pi * j)
            point3D = {'x': 0, 'y': 0, 'z': 0}
            point3D['x'] = x
            point3D['y'] = y
            point3D['z'] = z
            listpoint.append(point3D)
            j = j + 0.05
        i = i + 0.05
            
    return listpoint

def Tor(R ,r):
    listpoint = []
    pi = math.pi
    i = 0
    while i < 2:
        j = 0
        z = r * math.sin(pi * i)
        while j < 2:
            x = (R + r * math.cos(pi * i)) * math.sin(pi * j)
            y = (R + r * math.cos(pi * i)) * math.cos(pi * j)
            point3D = {'x': 0, 'y': 0, 'z': 0}
            point3D['x'] = x
            point3D['y'] = y
            point3D['z'] = z
            listpoint.append(point3D)
            j = j + 0.05
        i = i + 0.05
            
    return listpoint

# =========== End Figure ===========

# =========== Print ===========
def Print ():
    global figure, cavans
    cavans.delete("all") 
    i = -1
    for point3D in figure:
        point0 = Convert2D(figure[i])
        point1 = Convert2D(point3D)
        i = i + 1

        x0 = point0['x'] 
        y0 = point0['y'] 

        x1 = point1['x'] 
        y1 = point1['y']

        cavans.create_line(x0, y0, x1, y1)

def Convert2D (point3D):
    global af, bt, gm, k, width, height
    # x = point3D['x'] * math.cos(gm) - point3D['y'] * math.sin(gm) + width / 2 + dx
    # y = math.sin(af) * (point3D['x'] * math.sin(gm) + point3D['y'] * math.cos(gm)) + point3D['z'] * math.cos(af) + height / 2 + dy

    x = point3D['x']
    y = point3D['y']
    z = point3D['z']

    bx = k * (math.cos(gm) * (x*math.cos(bt) + z*math.sin(bt)) - y*math.sin(gm)) + width / 2 + dx
    by = k * (math.sin(af) * (y*math.cos(gm) + math.sin(gm) * (x*math.cos(bt) + z*math.sin(bt))) + math.cos(af) * (z*math.cos(bt) - x*math.sin(bt))) + height / 2 + dy

    point = {'x' : bx, 'y' : by}
    return point
# =========== End Print ===========

# =========== Form ===========
if __name__ == "__main__":
    root = Tk()
    figure = []
    
    root.iconbitmap('source/3d-model.ico')
    root.title('3DVision')
    root.configure(background='#89DAA4')
    root.resizable(width=False, height=False)

    # =========== Image ===========
    imgBall = ImageTk.PhotoImage(file = "source/orange.png")
    imgPear = ImageTk.PhotoImage(file = "source/pear.png")
    imgTor = ImageTk.PhotoImage(file = "source/donut.png")

    imgUp = ImageTk.PhotoImage(file = "source/up-arrow.png")
    imgDown = ImageTk.PhotoImage(file = "source/down-arrow.png")
    imgRight = ImageTk.PhotoImage(file = "source/right-arrow.png")
    imgLeft = ImageTk.PhotoImage(file = "source/left-arrow.png")
    imgRightAround = ImageTk.PhotoImage(file = "source/right-curved-arrow.png")
    imgLeftAround = ImageTk.PhotoImage(file = "source/left-curved-arrow.png")
    imgPlus = ImageTk.PhotoImage(file = "source/plus.png")
    imgMinus = ImageTk.PhotoImage(file = "source/minus.png")
    imgHome = ImageTk.PhotoImage(file = "source/home.png")
    # =========== End Image ===========

    # =========== Button ===========
    btnBall = Button(text = "Шар", width = 70, height = 35, image = imgBall, command = btnBall_Click)
    btnBall.grid(row = 0, column = 0, columnspan = 2, pady=(10, 10))

    btnPear = Button(text = "Груша", width = 70, height = 35, image = imgPear, command = btnPear_Click)
    btnPear.grid(row = 0, column = 2, columnspan = 2)

    btnTor = Button(text = "Тор", width = 70, height = 35, image = imgTor, command = btnTor_Click)
    btnTor.grid(row = 0, column = 4, columnspan = 2)

    # =========== Moving ===========
    btnZoomReduce = Button(text = "-", width = 35, height = 35, image = imgMinus, command = btnZoomReduce_Click)
    btnZoomReduce.grid(row = 3, column = 0, sticky = E, pady=(5, 5))   
    
    btnUp = Button(text = "Вверх", width = 35, height = 35, image = imgUp, command = btnUp_Click)
    btnUp.grid(row = 3, column = 1, pady=(5, 5))

    btnZoomIncrease = Button(text = "+", width = 35, height = 35, image = imgPlus, command = btnZoomIncrease_Click)
    btnZoomIncrease.grid(row = 3, column = 2, sticky = W, pady=(5, 5))

    btnLeft = Button(text = "Влево", width = 35, height = 35, image = imgLeft, command = btnLeft_Click)
    btnLeft.grid(row = 4, column = 0, sticky = E, pady=(5, 5))

    btnHome = Button(text = "Домой", width = 35, height = 35, image = imgHome, command = btnHome_Click)
    btnHome.grid(row = 4, column = 1, pady=(5, 5)) 

    btnRight = Button(text = "Вправо", width = 35, height = 35, image = imgRight, command = btnRight_Click)
    btnRight.grid(row = 4, column = 2, sticky = W, pady=(5, 5))

    btnDown = Button(text = "Вниз", width = 35, height = 35, image = imgDown, command = btnDown_Click)
    btnDown.grid(row = 5, column = 1, pady=(5, 10))
    # =========== End Moving ===========

    # =========== Rotation ===========
    btnLeftAround = Button(text = "", width = 35, height = 35, image = imgLeftAround, command = btnLeftAround_Click)
    btnLeftAround.grid(row = 3, column = 3, sticky = E, pady=(5, 5))

    btnUpRot = Button(text = "Вверх", width = 35, height = 35, image = imgUp, command = btnUpRot_Click)
    btnUpRot.grid(row = 3, column = 4, pady=(5, 5))

    btnRightAround = Button(text = "", width = 35, height = 35, image = imgRightAround, command = btnRightAround_Click)
    btnRightAround.grid(row = 3, column = 5, sticky = W, pady=(5, 5))

    btnLeftRot = Button(text = "Влево", width = 35, height = 35, image = imgLeft, command = btnLeftRot_Click)
    btnLeftRot.grid(row = 4, column = 3, sticky = E, pady=(5, 5)) 

    btnHomeRot = Button(text = "Домой", width = 35, height = 35, image = imgHome, command = btnHomeRot_Click)
    btnHomeRot.grid(row = 4, column = 4, pady=(5, 5)) 

    btnRightRot = Button(text = "Вправо", width = 35, height = 35, image = imgRight, command = btnRightRot_Click)
    btnRightRot.grid(row = 4, column = 5, sticky = W, pady=(5, 5))

    btnDownRot = Button(text = "Вниз", width = 35, height = 35, image = imgDown, command = btnDownRot_Click)
    btnDownRot.grid(row = 5, column = 4, pady=(5, 10))
    # =========== End Rotation ===========
    # =========== End Button ===========

    # =========== Canvas ===========
    cavans = Canvas(root, width = width, height = height, bg='white')
    cavans.grid(row = 1, column = 0, columnspan = 6, padx=(10, 10))
    # =========== End Canvas ===========

    # =========== Label ===========
    lbDebug = Label(text = 'Перемещение', width = 25,  font=("Areal", 12, "bold"))
    lbDebug.grid(row = 2,  column = 0, columnspan = 3, pady=(10, 5))

    lbDebug = Label(text = 'Поворот', width = 25, font=("Areal", 12, "bold"))
    lbDebug.grid(row = 2,  column = 3, columnspan = 3, pady=(10, 5))
    # =========== End Label ===========                     
 
    root.mainloop()
# =========== End Form ===========
