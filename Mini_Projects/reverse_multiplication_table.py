# Reverse Multiplication Table

number = int(input("Please enter the Number\n"))

print("The Multiplication table of number", number, "is:")
for i in range(10,0,-1):
    print(number, "multiplied by", i, 'is equal to', (number * i))
else:
    print("Done")