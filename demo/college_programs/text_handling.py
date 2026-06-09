def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    return len(text)

def reverse_text(text):
    return text[::-1]

def capitalize_text(text):
    return text.upper()

def find_substring(text, substring):
    if substring in text:
        return "The substring " + substring + " is found in the text."
    else:
        return f"The substring '{substring}' is not found in the text."

input_text = input("Enter some text: ")
print(f"Number of words: {count_words(input_text)}")
print(f"Number of characters: {count_characters(input_text)}")
print(f"Reversed text: {reverse_text(input_text)}")
print(f"Capitalized text: {capitalize_text(input_text)}")

substring = input("Enter a substring to search for: ")
print(find_substring(input_text, substring))