import math  # Import the math module (not used here, but often used for math operations)

class shape:  # Define a base class for shapes
    def __init__(self, name):  # This function runs when we create a new shape
        self.name = name  # Store the name of the shape
    def get_area(self):  # Define a function to get the area of the shape
        return 0  # Default area is 0, to be overridden by subclasses
    
class circle(shape):  # Define a class for circles, based on shape
    def __init__(self, name, radius):  # This function runs when we create a new circle
        super().__init__(name)  # Call the parent class (shape) constructor with the name
        self.radius = radius # Store the radius of the circle
    def get_area(self):  # Define a function to calculate the area of the circle
        pi = 3.14  # Define the value of pi (approximate)
        return pi * self.radius ** 2  # Calculate the area using the formula πr^2

class rectangle(shape):  # Define a class for rectangles, based on shape
    def __init__(self, name, width, height):  # This function runs when we create a new rectangle
        super().__init__(name)  # Call the parent class (shape) constructor with the name
        self.width = width  # Store the width of the rectangle
        self.height = height  # Store the height of the rectangle
    def get_area(self):  # Define a function to calculate the area of the rectangle
        return self.width*self.height  # Calculate the area using the formula width * height
    
# Create instances of your shapes
circle = circle("My Circle", 5)  # Create a circle with name and radius
rectangle = rectangle("My Rectangle", 4, 6)  # Create a rectangle with name, width, and height
generic_shape = shape("Just a Shape")  # Create a generic shape with just a name

# Put them in a list of mixed types
shapes = [circle, rectangle, generic_shape]  # Store all shapes in a list

# Iterate through the list and call get_area() on each.
# Notice how the *same* method call (shape.get_area()) behaves differently
# depending on the actual type of the object. This is polymorphism!
for shape in shapes:  # Go through each shape in the list
    print(f"{shape.name} Area: {shape.get_area():.2f}")  # Print the name and area of each shape, formatted to 2 decimal places

# Expected Output:
# My Circle Area: 78.54
# My Rectangle Area: 24.00
# Just a Shape Area: 0.00