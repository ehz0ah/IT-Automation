import re

print(re.search(r"Py.*n", "Pygmalion"))  # . multiplied repeatedly until you reach a 'n' character
print(re.search(r"Py.*n", "Python Programming"))  # Does not stop at 'Python' but at 'Programmin', * takes in as many char as possible
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Pyn"))   # Match lower letters only but also allow zero char

print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))  # The plus character matches one or more occurrences of the character that comes before it.
print(re.search(r"o+l+", "boil"))  # Got i so return None

print(re.search(r"p?each", "To each their own"))  # It means either zero or one occurrence of the character before it.
print(re.search(r"p?each", "I like peaches"))
