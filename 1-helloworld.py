print("Hello, World!")
name = "deba"
name1 = 10.000
print( type(name))
print( type(name1))

height = 5.9
print(type(height))
## create multiline string
multiline_string = """This is a multiline string.
It can span multiple lines."""
print(f"Multiline String:\n{len(multiline_string)} characters")
print(f"Multiline String:\n{multiline_string.index('multiline')}")
print(f"Multiline String:\n{multiline_string.count('multilin')}")
multiline_string = multiline_string.replace("multiline", "multi-line")
print(f"Replace check:\n{multiline_string}")
split_string = multiline_string.split()
for char in split_string:
    print(char)

