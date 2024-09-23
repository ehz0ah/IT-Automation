import re

# Inside the [] is the condition you restrict the wildcard to have

print(re.search(r"[Pp]ython", "Python")) 

print(re.search(r"[a-z]way", "The end of the highway"))  # This just means the wildcard is all lowercase characters
print(re.search(r"[a-z]way", "What a way to go"))
print(re.search("cloud[a-zA-Z0-9]", "cloudy"))         # Combination of numbers, lower and upper characters
print(re.search("cloud[a-zA-Z0-9]", "cloud9"))

print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))  # Use ^ to match characters not in the []
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))  # This one includes spaces

print(re.search(r"cat|dog", "I like cats."))             # Pipe symbol | means search for either one
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))  # After it found dogs, it won't find cats
print(re.findall(r"cat|dog", "I like both dogs and cats."))  # re.findall finds all occurrences