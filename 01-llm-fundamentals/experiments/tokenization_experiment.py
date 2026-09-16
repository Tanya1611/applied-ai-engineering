import tiktoken
import csv

def record_token_data(inputText: str, model_name="gpt-4o-mini"):

    # Load the encoding(tokenizer) for the model
    encoder = tiktoken.encoding_for_model(model_name)

    # Get the integer Token ID
    token_ids = encoder.encode(inputText)

    # Calculate the Token Count
    token_count = len(token_ids)

    # Decode each token individually to see the actual text pieces
    actual_tokens = [encoder.decode([tid]) for tid in token_ids]
    
    # Print the output in the console
    print(f"---> Token Report for '{inputText}' <---")
    print(f"Text: {inputText}")
    print(f"Token Count: {token_count}")
    print(f"Actual Tokens: {actual_tokens}\n")

    # Save the data to a CSV file
    file_name = "01-llm-fundamentals/experiments/token_records.csv"
    with open(file_name, mode="a", newline="") as file:
        writer = csv.writer(file)
        
        # Write header if file is empty
        if file.tell() == 0:
            writer.writerow(["Text", "Token Count", "Actual Tokens"])
            
        # Write the data row (Actual Tokens saved as a comma-separated string)
        writer.writerow([inputText, token_count, ", ".join(actual_tokens)])
    
    print(f"Successfully recorded to {file_name}!\n\n")

record_token_data("Hello world")
record_token_data("I am learning AI Engineering.")
record_token_data("Artificial intelligence")
record_token_data("customer_support_ticket_12345")
record_token_data('''def calculate_interest(principal, rate): 
    return principal * rate
''')



"""
--------------------------------INSIGHT------------------------------------------

I observed that human words and model tokens are not equivalent. (Specially refer last two input text results.")
This matters in application design because token count determines how much input/context can fit into the model's context budget and contributes to inference cost.


---------------------------------OUTPUT------------------------------------------

---> Token Report for 'Hello world' <---
Text: Hello world
Token Count: 2
Actual Tokens: ['Hello', ' world']

Successfully recorded to 01-llm-fundamentals/experiments/token_records.csv!


---> Token Report for 'I am learning AI Engineering.' <---
Text: I am learning AI Engineering.
Token Count: 6
Actual Tokens: ['I', ' am', ' learning', ' AI', ' Engineering', '.']

Successfully recorded to 01-llm-fundamentals/experiments/token_records.csv!


---> Token Report for 'Artificial intelligence' <---
Text: Artificial intelligence
Token Count: 2
Actual Tokens: ['Artificial', ' intelligence']

Successfully recorded to 01-llm-fundamentals/experiments/token_records.csv!


---> Token Report for 'customer_support_ticket_12345' <---
Text: customer_support_ticket_12345
Token Count: 6
Actual Tokens: ['customer', '_support', '_ticket', '_', '123', '45']

Successfully recorded to 01-llm-fundamentals/experiments/token_records.csv!
----------------------------------------------------------------------------------
"""