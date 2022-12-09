from tkinter import *
from math import *

def calcArea(w,h):
    return w*h

def calcPerimeter(w,h):
    return 2*w + 2*h

def calcRadius(r):
    rad = pi * r**2
    ius = "{:.2f}".format(rad)
    return ius

def calcTriangle(w,h):
    return (w*h)/2

def calcCircleP(r):
    rad = 2*pi*r
    ius = "{:.2f}".format(rad)
    return ius

def calcTriangleP(s1,s2,s3):
    return s1+s2+s3

def clickArea():
    area.set(calcArea(height.get(), width.get()))
def clickPerimeter():
    area.set(calcPerimeter(height.get(), width.get()))
def clickRadius():
    area.set(calcRadius(radius.get()))
def clickTriangle():
    area.set(calcTriangle(height.get(), width.get()))
def clickCircleP():
    area.set(calcCircleP(radius.get()))
def clickTriangleP():
    area.set(calcTriangleP(side1.get(), side2.get(), side3.get()))

root = Tk()
root.title("Calculate Area or Perimeter")
width = IntVar()
height = IntVar()
area = IntVar()
perimeter = IntVar()
radius = IntVar()
side1 = IntVar()
side2 = IntVar()
side3 = IntVar()

Label(root, text="Width").grid(row=0, column=0)
Entry(root, textvariable=width).grid(row=0, column=1)

Label(root, text="Height").grid(row=1, column=0)
Entry(root, textvariable=height).grid(row=1, column=1)

Label(root, text="Radius").grid(row=5, column=0)
Entry(root, textvariable=radius).grid(row=5, column=1)

Label(root, text="Triangle: Side 1").grid(row=8, column=0)
Entry(root, textvariable=side1).grid(row=8, column=1)
Label(root, text="Triangle: Side 2").grid(row=9, column=0)
Entry(root, textvariable=side2).grid(row=9, column=1)
Label(root, text="Triangle: Side 3").grid(row=10, column=0)
Entry(root, textvariable=side3).grid(row=10, column=1)

Label(root, text="Result").grid(row=12, column=0)
Label(root, textvariable=area).grid(row=12, column=1)

button = Button(root, text="Calculate Area of Square/Rectangle", command=clickArea)
button1 = Button(root, text="Calculate Area of Circle", command=clickRadius)
button2 = Button(root, text="Calculate Area of Triangle", command=clickTriangle)
button3 = Button(root, text="Calculate Perimeter of Square/Rectangle", command=clickPerimeter)
button4 = Button(root, text="Calculate Perimeter of Circle", command=clickCircleP)
button5 = Button(root, text="Calculate Perimeter of Triangle", command=clickTriangleP)
button.grid(row=2, column=0, columnspan=2)
button1.grid(row=6, column=0, columnspan=2)
button2.grid(row=4, column=0, columnspan=2)
button3.grid(row=3, column=0, columnspan=2)
button4.grid(row=7, column=0, columnspan=2)
button5.grid(row=11, column=0, columnspan=2)
root.mainloop()