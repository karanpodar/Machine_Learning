# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    sums = []
    runningsum(root, 0, sums)
    return sums

def runningsum(node, runsum, sums):
    if node == None:
        return
    runsum += node.value
    
    if node.left == None and node.right == None:
        sums.append(runsum)
        return

    runningsum(node.left, runsum, sums)
    runningsum(node.right, runsum, sums)
