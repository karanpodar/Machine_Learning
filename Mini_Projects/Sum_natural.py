# Sum of n Natural number using while loop

num = int(input('Please enter the number'))
i = 1
sum = 0
while i<num+1 :
    sum = sum + i
    i = i + 1 

print(f"The sum of first {num} natural numbers is {sum}")
    