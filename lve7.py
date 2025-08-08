class DataProcessor:  # Define a base class for processing data
    def __init__(self, data):  # This function runs when we create a new DataProcessor
        self.data = data  # Store the data in the object
    def process_data(self):  # Define a function to process the data
        raise NotImplementedError("This method should be overridden by subclasses")  # Force subclasses to implement this method
        
    
class CVProcessor(DataProcessor):  # Define a class for processing CSV-like data, based on DataProcessor
    def __init__(self, data):  # This function runs when we create a new CVProcessor
        super().__init__(data)  # Call the parent class constructor to store the data
    def process_data(self):  # Define a function to process CSV data
        return self.data.split(",")  # Split the data by commas and return a list of items
    


class JsonProcessor(DataProcessor):  # Define a class for processing JSON-like data, based on DataProcessor
    def __init__(self, data):  # This function runs when we create a new JsonProcessor
        super().__init__(data)  # Call the parent class constructor to store the data
    
    def process_data(self):
        # 1. Start with an empty dictionary
        result_dict = {}

        # 2. Strip any leading/trailing spaces or braces
        cleaned_data = self.data.strip().strip('{}')

        # 3. Split into a list of "key:value" pairs
        key_value_pairs = cleaned_data.split(',')

        # 4. Loop through the list of pairs
        for pair in key_value_pairs:
            # 5. Inside the loop, split each pair by the colon
            key_value_list = pair.split(':')
            key = key_value_list[0]
            value = key_value_list[1]

            # 6. Clean up the key and value strings (strip spaces and single quotes)
            cleaned_key = key.strip().strip("'")
            cleaned_value = value.strip().strip("'")
            
            # 7. Add the cleaned key-value pair to your dictionary
            result_dict[cleaned_key] = cleaned_value

        # 8. Return the final dictionary
        return result_dict

# Create instances of your data processors
csv_data = "apple,banana,cherry"  # Example CSV data as a string
json_data = "'name':'John', 'age':'30'"  # Example JSON-like data as a string

csv_processor = CVProcessor(csv_data)  # Create a CVProcessor with the CSV data
json_processor = JsonProcessor(json_data)  # Create a JsonProcessor with the JSON-like data

# Put them in a list of mixed types
processors = [csv_processor, json_processor]  # Store both processors in a list

# Iterate and process the data.
# Each processor handles its specific data format with the same method call.
for processor in processors:  # Go through each processor in the list
    processed_output = processor.process_data()  # Process the data using the processor's method
    print(f"Original Data: '{processor.data}'")  # Print the original data
    print(f"Processed Output Type: {type(processed_output)}")  # Print the type of the processed output (should be list)
    print(f"Processed Data: {processed_output}\n")  # Print the processed data

# Expected Output:
# Original Data: 'apple,banana,cherry'
# Processed Output Type: <class 'list'>
# Processed Data: ['apple', 'banana', 'cherry']

# Original Data: "'name':'John', 'age':'30'"
# Processed Output Type: <class 'dict'>
# Processed Data: {'name': 'John', 'age': '30'}