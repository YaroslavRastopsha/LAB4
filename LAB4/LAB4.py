# Зробив Растопша Ярослав КН33
import string

# Original text
text = "Glukhiv is a small town in northern Ukraine with a rich historical heritage. In the 18th century, it served as the capital of Left-Bank Ukraine and was known as a cultural and educational center of that time. Glukhiv played a significant role in the development of Ukrainian culture and science. Today, the town preserves many architectural monuments, including the Transfiguration Church and St. Nicholas Cathedral. It is also known for its educational institutions, with Glukhiv National Pedagogical University named after Oleksandr Dovzhenko being one of the oldest universities in Ukraine."

# 1. Convert all text to lowercase
lowercase_text = text.lower()

# 2. Remove punctuation
no_punctuation_text = lowercase_text.translate(str.maketrans('', '', string.punctuation))

# 3. Split text into words
words_list = no_punctuation_text.split()

# 4. Replace the word 'glukhiv' with 'town'
replaced_text = no_punctuation_text.replace("glukhiv", "town")

# Output results
print("Lowercase text:", lowercase_text)
print("Text without punctuation:", no_punctuation_text)
print("List of words:", words_list)
print("Replaced text:", replaced_text)

