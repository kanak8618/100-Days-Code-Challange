# Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have an area function which can print the area of the shape where Shape's area is 0 by default

class Shape:
    def __init__(self):
        pass # Default constructor, no need to initialize anything
    def area(self):
        return 0 # Shape's area is 0 by default
class Square(Shape):
    def __init__(self, length):
        super().__init__() # Call the constructor of the parent class
        self.length = length
    def area(self):
        return self.length ** 2 # Calculate the area of the square
shape = Shape()
square = Square(float(input("Enter the shape of the square: ")))
print("Shape's area by default:", shape.area()) 
print("Area of the square:", square.area()) 
