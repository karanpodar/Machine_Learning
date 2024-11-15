def nodeDepths(root):
    sums = 0
    stack = [{'node' : root, 'depth' : 0}]
    while len(stack) > 0:
        stack_info = stack.pop()
        node, depth = stack_info['node'], stack_info['depth']
        print(node,depth)
        # if node is None:
        #     continue
        sums += depth
        if node.left != None:
            stack.append({'node' : node.left, 'depth' : depth+1})
        if node.right != None:
            stack.append({'node' : node.right, 'depth' : depth+1})
    return sums


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
