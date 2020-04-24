# stack using list
class stackoperations:
    stack =[]
    text = input("Please enter some input text")
    check = input("Are you done?")
    check = check.lower()
    stack.append(text)
    popping = stack.pop()
    print(popping)
## stack implementation using library methods

from _collections import deque
