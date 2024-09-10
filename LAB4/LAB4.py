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
# Зробив Григоренко Максим  КН33
# 5. Перетворюємо перше слово на велике, інші на малі
capitalized_text = replaced_text.capitalize()

# 6. Шукаємо перше входження слова "cat" в тексті
index_of_cat = replaced_text.find("cat")

# 7. Рахуємо кількість входжень слова "the" в тексті
count_of_the = replaced_text.count("the")
print("Capitalized text:", capitalized_text)
print("Index of 'cat':", index_of_cat)
print("Count of 'the':", count_of_the)
#Зробив Узжин Роман КН-33
#8. Replace all occurrences of 'ukraine' with 'country'
replaced_ukraine_text = replaced_text.replace("ukraine", "country")

# 9. Count the number of words in the text
word_count = len(words_list)

# 10. Check if all words consist only of letters
all_words_are_alpha = all(word.isalpha() for word in words_list)

print("Text with 'Ukraine' replaced by 'country':", replaced_ukraine_text)
print("Word count:", word_count)
print("All words consist only of letters:", all_words_are_alpha)

# Зробив Головенко Марк  КН33
# 11. Використовуємо string.capwords для перетворення тексту на формат заголовка
capwords_text = string.capwords(no_punctuation_text)

# 12. Використовуємо string.Template для роботи з шаблоном
template = string.Template("The $animal jumps over the $object.")
template_text = template.substitute(animal="cat", object="moon")

# 13. Використовуємо string.hexdigits для отримання всіх шістнадцяткових цифр
hexdigits = string.hexdigits

print("Capwords text:", capwords_text)
print("Template text:", template_text)
print("Hexadecimal digits:", hexdigits)
