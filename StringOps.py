f = open("alice.txt", "r")

text = f.read()
print(text.count('Alice'))
print(text.split("Alice", 12))
print(len(text.split("Alice", 12)))
