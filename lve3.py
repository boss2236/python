def find_max_value(numbers):  # Define a function that finds the largest number in a list
    """Returns the maximum value in a list."""  # This is a description of what the function does
    if not numbers:  # Check if the list is empty
        return None  # If the list is empty, return None (no value)
    max_value = numbers[0]  # Assume the first number is the largest for now
    for value in numbers:  # Go through each number in the list
        if value > max_value:  # If the current number is bigger than our current largest
            max_value = value  # Update the largest number
    return max_value  # After checking all numbers, return the largest one found

# Part 1 Usage
numbers = [1, 5, 2, 8, 3]  # Create a list of numbers
print(f"The maximum value is: {find_max_value(numbers)}") # Print out the largest number in the list (should be 8)

class shopping_list:  # Define a class to represent a shopping list
    def __init__(self):  # This function runs when we create a new shopping list
       self.items = []  # Start with an empty list of items
    
    def add_item(self, item):  # Define a function to add an item to the shopping list
        self.items.append(item)  # Add the given item to the list

    def remove_item(self, item):  # Define a function to remove an item from the shopping list
        if item in self.items:  # Check if the item is in the list
            self.items.remove(item)  # If it is, remove it

    def get_total_items(self):  # Define a function to count how many items are in the list
        return len(self.items)  # Return the number of items in the list
    
# Part 2 Usage
my_list = shopping_list()  # Create a new shopping list
my_list.add_item("Milk")  # Add "Milk" to the shopping list
my_list.add_item("Bread")  # Add "Bread" to the shopping list
my_list.add_item("Eggs")  # Add "Eggs" to the shopping list
print(f"Total items after adding: {my_list.get_total_items()}") # Print how many items are in the list (should be 3)

my_list.remove_item("Bread")  # Remove "Bread" from the shopping list
print(f"Total items after removing bread: {my_list.get_total_items()}") # Print how many items are left (should be 2)