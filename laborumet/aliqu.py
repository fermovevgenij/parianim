def initialize_fields():
    # Initialize input field
    input_field = ""

    # Initialize output field
    output_field = ""

    return input_field, output_field

# Initialize fields
input_field, output_field = initialize_fields()

# Example usage
input_field = input("Enter some text: ")
output_field = f"You entered: {input_field}"
print(output_field)
