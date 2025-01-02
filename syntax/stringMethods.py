# .find() - > Returns the first occurence of a given character
# .rfind() - > Returns the last occurence of a given character

import re

string = "123-456-7890"


name = input("Enter your full name: ")
print(name)

firstE = name.find("e")
lastE = name.rfind("e")

if firstE == -1:
    firstE = "We couldnt find that"
if lastE == -1:
    lastE = "We couldnt find that"


print("The positon of the first E: ")

print(firstE)

print("The positon of the last E: ")

print(lastE)


print("Number of characters: ")
result = len(name.replace(" ", ""))
print(result)


