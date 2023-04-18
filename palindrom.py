import re

def is_palindrome(sentence):
    # Check if input is a string
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string.")
        
    # Remove all punctuation and spaces, and convert to lowercase
    sentence = re.sub(r'[^\w\s]', '', sentence).replace(' ', '').lower()
    
    # Check if the sentence is the same backwards and forwards
    return sentence == sentence[::-1]

# Example usage
sentence = input("type the sentence: ")
try:
    if is_palindrome(sentence):
        print(f"{sentence} is a palindrome!")
    else:
        print(f"{sentence} is not a palindrome.")
except TypeError as e:
    print(f"Error: {e}")
