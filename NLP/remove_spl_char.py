'''
special character - @ # %....
'''

string = "K@r@n !s $#%"
 
test_str = ''.join(letter for letter in string if letter.isalnum())
print(test_str)