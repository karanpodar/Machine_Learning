# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    curr = linkedList

    while curr is not None:
        nextdist = curr.next
        while nextdist is not None and curr.value == nextdist.value:
            nextdist = nextdist.next
        curr.next = nextdist
        curr = nextdist
    
    return linkedList
