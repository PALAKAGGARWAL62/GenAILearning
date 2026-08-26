"""
1. capitalize_words(text) -> return text with each word capitalized
2. reverse_string(text) -> return reversed string
3. word_count(text) -> return number of words in the text
"""

def capitalize_words(word):
    return word.upper()

def reverse_string(word):
    return word[::-1]

def word_count(text):
    words = text.split(' ')
    return len(words)
