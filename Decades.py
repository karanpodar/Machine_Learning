
#Convert Age to Decades & Years

age = int(input("How old are you?\n"))
decades = age//10
years = age % 10

print ("You are " + str(decades) + " decades and " + str(years) + " years old." )