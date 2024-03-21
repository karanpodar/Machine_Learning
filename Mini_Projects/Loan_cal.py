# Loan Calculator

money_owed = float(input("How much money do you owe?\n"))
apr = float(input("How much is Annual Percentage Rate?\n"))
#payment = float(input("How much will you pay monthly?\n"))
months = int(input("How many months you want to pay??\n"))

monthly_rate = (apr/100)*(months//12)

#Calculate the interest to pay each month
monthly_interest = money_owed*monthly_rate

#Calculate the total amount
money_owed = money_owed + monthly_interest
print ("Total amount paid", money_owed)

#Calculate EMI
payment = money_owed/months

print ("The EMI for your loan will be ", payment, " for ", months, "months", sep = '')