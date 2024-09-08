'''
Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 
'''

def merge_list(list1, list2):

    output = []
    max_len = max(len(list1),len(list2))
    count = 0
    i = 0
    j = 0

    if len(list1) == len(list2) == 0:
        return []
    elif len(list1) == 0:
        return list2
    elif len(list2) == 0:
        return list1
        
    while count < max_len:
        print('i', i)
        print('j', j)
        if list1[i] == list2[j]:
            output.append(list1[i])
            output.append(list2[j])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            output.append(list1[i])
            i += 1
        else:
            output.append(list2[j])
            j += 1

        count = min(i,j)
    
    return output

list1 = [1,2,4]
list2 = [1,3,4]

print(merge_list(list1, list2))

list1 = []
list2 = []

print(merge_list(list1, list2))

list1 = []
list2 = [0]

print(merge_list(list1, list2))