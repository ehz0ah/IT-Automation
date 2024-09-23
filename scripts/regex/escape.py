import re

print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "mydomain.com"))  # Escape character

print(re.search(r"\w*", "This is an example"))  # Space not included in \w
print(re.search(r"\w*", "And_this_is_another"))  # \w matches any alphanumeric character including letters, numbers, and underscores.

# There's also \d for matching digits
# \s for matching whitespace characters like space, tab or new line
# \b for word boundaries
