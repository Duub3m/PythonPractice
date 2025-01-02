# string = input("Enter your name")
# string = string.replace(" ", "")
max_score = 0
string = "011101"
for index in range(1, len(string)):
    left = string[:index]
    print(left)
    right = string[index:]
    print(right)

    score = left.count("0") + right.count("1")
    max_score = max(max_score, score)

print(max_score)