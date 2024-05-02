def linear_search(input_list, num):
    
    for index, value in enumerate(input_list):
       
        if value == num:
            return index

    return None
        
input_list = [1, 5, 9, 3]
num = 7

print(linear_search(input_list, num))