arr1 = [10, 5, 2, 6, 5, 5]

def subarry(arr1):
    
    output = set()
    
    for i in range(0, len(arr1)):
      
        for j in range(i, len(arr1)):

            if i == j:
                output.add(arr1[j])
            else:
                # output.add(tuple(arr1[i:j+1]))      
                output.add(tuple(sorted(arr1[i:j+1])))    # to have sorted values 

    return output

print(subarry(arr1))
