
class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return  self.width * self.height
    def get_perimeter(self):
        return (self.width + self.height) *2
    
# Create a rectangle object
rectangle1 = rectangle(10, 5)

# Call its methods
print(f"Rectangle Area: {rectangle1.get_area()}")        # Expected: 50
print(f"Rectangle Perimeter: {rectangle1.get_perimeter()}")  # Expected: 30

rectangle2 = rectangle(2.5, 8.0)
print(f"Rectangle Area: {rectangle2.get_area()}")        # Expected: 20.0
print(f"Rectangle Perimeter: {rectangle2.get_perimeter()}")  # Expected: 21.0