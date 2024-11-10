# Loan Calculator


money_owed = float(input("How much money do you owe?\n"))
apr = float(input("How much is Annual Percentage Rate?\n"))
months = int(input("How many months you want to pay??\n"))
amount_paid = float(0)

monthly_rate = (apr/100)*(months//12)

#Calculate the interest to pay each month
monthly_interest = money_owed*monthly_rate
    
#Calculate the total amount
money_owed = money_owed + monthly_interest
print ("Total amount to be paid", money_owed)

#Calculate EMI
payment = money_owed/months

for i in range(months-1):    
    
    #Calculate Paid amount after each month
    amount_paid = amount_paid + payment

    #Calculate Pending amount after each month
    amount_pending = money_owed - amount_paid
    
    print ("The pending loan amount after", i+1, end = ' ')
    print ("months is", amount_pending)

print ("The EMI for your loan will be ", payment, " for ", months, "months", sep = '')