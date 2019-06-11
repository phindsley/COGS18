"""A collection of functions from my project."""

def is_question(input_string):
    """Check if it is a question."""
    
    if '?' in input_string:
        output = True
    else:
        output = False
        
    return output

def remove_punctuation(input_string):
    """Get rid of punctuation once it is known as a question."""
    
    out_string = ''
    for char in input_string:
        if char not in string.punctuation:
            out_string = out_string + char
    return out_string

def prepare_text(input_string):
    """Prepare the text inputs for processing."""
    
    temp_string = input_string.lower()
    
    temp_string = remove_punctuation(temp_string)
    
    out_list = temp_string.split()
    
    return out_list

def selector(input_list, check_list, return_list):
    """Selects an output for the chatbot."""

    output = None
    
    for item in input_list:
        if item in check_list:
            output = random.choice(return_list)
            
            break
            
    return output

def string_concatenator(string1, string2, separator):
    """Concatenates two strings and combines them with a separator."""
    
    if string1 and string2 is None:
        output = None
    else:
        output = string1 + separator + string2
        
    return output

def list_to_string(input_list, separator):
    """Turn a list of strings back into one single concatenated string."""
    
    output = input_list[0]
    
    for item in input_list[1:]:
        output = string_concatenator(output, item, separator)
        
        return output
    
def end_chat(input_list):
    """Ends the chat."""
    
    if 'quit' in input_list:
        output = True
    else:
        output = False
    
    return output