import string  # Import the string module to help with text processing (like removing punctuation)



class TextAnalyzer:  # Define a class to analyze text
    def __init__(self, text):  # This function runs when we create a new TextAnalyzer
        self.text = text  # Store the given text in the object
        
    def get_word_count(self):  # Define a function to count the number of words
        words = self.text  # Split the text into words (splits at spaces)
        words = words.translate(str.maketrans('', '', string.punctuation)).split()  # Remove punctuation from each word
        words = [word.lower() for word in words]    # Convert each word to lowercase
        return len(words)  # Return how many words there are
    
    def get_unique_words(self):  # Define a function to count unique words
        words = self.text  # Split the text into words
        words = words.translate(str.maketrans('', '', string.punctuation)).split()  # Remove punctuation from each word
        words = [word.lower() for word in words]  # Convert each word to lowercase
        unique_words = set(words)  # Convert the list of words to a set (removes duplicates)
        return unique_words  # Return how many unique words there are
    

analyzer = TextAnalyzer("Hello world! This is a test. Hello Python world.")  # Create a TextAnalyzer with some text

print(f"Total words: {analyzer.get_word_count()}")     # Print the total number of words (should be 9)
print(f"Unique words: {analyzer.get_unique_words()}")   # Print the number of unique words (should be 7, after punctuation and case normalization)

analyzer2 = TextAnalyzer("One, two, three. One, two, four!")  # Create another TextAnalyzer with different text
print(f"Total words: {analyzer2.get_word_count()}")     # Print the total number of words (should be 6)
print(f"Unique words: {analyzer2.get_unique_words()}")   # Print the number of unique words (should be 4, after punctuation and case normalization)