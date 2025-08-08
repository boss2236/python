


numbers = [int(input(f"Enter number {i+1}: ")) for i in range(3)]


def sum_list_elements(numbers):    
    
    total = 0
    for number in numbers:        
        total += number
    
    return total
    
    


print(f"The sum of the numbers is: {sum_list_elements(numbers)}")
    



def calculate_circle_area(radius):
    pi = 3.14  # Define the value of pi
    return pi * radius ** 2  # Calculate the area using the formula πr²


radius = float(input("Enter the radius of the circle: "))
print(f"The area of the circle is: {calculate_circle_area(radius)}")
