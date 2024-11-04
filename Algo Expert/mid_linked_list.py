# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    # Write your code here.
    slow = linkedList
    fast = linkedList

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
    return slow
