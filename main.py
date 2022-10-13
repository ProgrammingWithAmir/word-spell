"""
    Spell Checker Program Using Python
"""

# Importing Modules 
from textblob import TextBlob

# Incorrect spelling
word = str(input("Enter the word to be checked : "))

# Shows the original text
print("original text : " + word)

# Correcting the text
correct_word = TextBlob(word)

# Shows the corrected spelling
print("corrected text: "+ str(correct_word.correct()))

