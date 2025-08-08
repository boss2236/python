s = input("Enter a string: ")  # Ask the user to enter a string and store it in variable 's'

def reverse_string(s):  # Define a function to reverse a string
    if len(s) == 0:  # If the string is empty (base case)
        return s  # Return the empty string
    else:  # Otherwise
        return reverse_string(s[1:]) + s[0]  
    ''' Recursively reverse the substring starting from the second character, 
     then append the first character to the end. This builds the reversed 
     string step by step as the recursion unwinds.'''

print(f"The reversed string is: {reverse_string(s)}")  # Print the reversed string using the function