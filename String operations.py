
sentence = input('Enter a string of at least 10 characters')
sentence = str(sentence)

print("Capital word:", sentence.capitalize())
print("Casefold:", sentence.casefold())
print("Center operation:", sentence.center(2, '*'))
print("Count:", sentence.count(sentence.casefold()))
print("Encoded version of string:", sentence.encode(encoding='utf-8', errors='ignore'))
print("Ends with operation, to check if it ends with a:", sentence.endswith(('a', 'y')))
print("Find operation:", sentence.find('an', 1, len(sentence)-1))
print("Every {3} should know the use of {2} {1} programming and {0}".format('animal', 'computer', 'c++', 'GK'))
print("{0:^16} was founded in {1:<4}!".format("GeeksforGeeks", 2009))
print('Replace operation:', sentence.replace('aditya', 'anupama'))
