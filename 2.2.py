string = "a f f h d e e e g g d s g h f d s f g d".split()

chars = []

for unique_char in set(string):
    newlist = [char for char in string if char == unique_char]
    chars.append(newlist)

print(chars)