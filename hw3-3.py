# A program that calculates the area of different shapes
# Date: 10/24/21
# Author: Kevin Owidi

import math
# menu function
def menu():
    print("Shape area Caculator")
    print("------------------------)")
    print("1. Square")
    print("2. Rectangle")
    print("3. Circle")
    shape = input("Choose a shape (1-3): ")
    return shape
# three functions for each shape
def square_area():
    side = float(input("Please enter the length of one side of the square "))
    area = side * side
    return area

def rectangle_area():
    length = float(input("Please enter the length of the rectangle: "))
    width = float(input("Please enter the width of the rectangle: "))
    area = length * width
    return area

def circle_area():
    radius = float(input("Please enter the radius of the circle: "))
    area = math.pi * math.pow(radius, 2)
    return area
# main program
shape = menu()
if shape == "1":
    area = square_area()
elif shape == "2":
    area = rectangle_area()
elif shape == "3":
    area = circle_area()
# display the area based on the shape of choice
print("The area of the chosen shape is: ", round(area, 2))