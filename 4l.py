import string  # Import the string module to handle punctuation

text= input("Enter a string: ")  # Ask the user to enter a string and store it in variable

def count_word_frequency(text):  # Define a function to count word frequency
    words = text.split()  # Split the string into words
    
    words = text.translate(str.maketrans('', '', string.punctuation)).split() 
    # Remove punctuation and split into words
    frequency = {}  # Initialize an empty dictionary to store word frequency
    for word in words:  # Iterate through each word
        word = word.lower()  # Convert the word to lowercase for case-insensitive counting
        if word in frequency:  # If the word is already in the dictionary
            frequency[word] += 1  # Increment its count
        else:
            frequency[word] = 1  # Otherwise, add it with a count of 1
    
    return frequency  # Return the dictionary containing word frequencies
    
print(f"The word frequency is: {count_word_frequency(text)}")  # Print the word frequency using the function

