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

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_list(list1, list2):

    head = ListNode()
 
    while list1 or list2:
        
        i = list1.val
        j = list2.val

        if i == j:
            list1.next = j
            list2 = list2.next

        elif i < j:
            list1 = list1.next
            
        else:
            list1.val = j
            list2 = list2.next

    return list1

list1 = [1,2,4]
list2 = [1,3,4]

print(merge_list(list1, list2))

list1 = []
list2 = []

print(merge_list(list1, list2))

list1 = []
list2 = [0]

print(merge_list(list1, list2))