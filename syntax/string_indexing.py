import re
ones=0
# (123)-5678-9012-3456
credit_number = input("What is your credit card number: ")

credit_number = re.sub(r"[-() ]", "", credit_number)

print(credit_number)

# credit_number = re. subsititute - for "" in credit_number
masked_credit_number = ""
for index, number in enumerate(credit_number):
    if index < len(credit_number) - 4:
        masked_credit_number += "X"
    else:
        masked_credit_number += number

print(masked_credit_number)

credit_number = "123567890123456"
masked_credit_number = "X" * (len(credit_number) - 4) + credit_number[-4:]
print(masked_credit_number)

# print the first four digits of the credit card number


