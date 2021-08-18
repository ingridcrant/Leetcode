class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bstFromPreorder(self, preorder):
    if len(preorder) == 0:
        return None
    elif len(preorder) == 1:
        return TreeNode(preorder[0])
    else:
        root = TreeNode(preorder[0])
        partitioned = self.partition(preorder)
        
        root.left = self.bstFromPreorder(partitioned[0])
        root.right = self.bstFromPreorder(partitioned[1])
        return root

def partition(self, arr):
    p = arr[0]
    partitioned = [[], []]

    for i in range(1, len(arr)):
        if arr[i] < p:
            partitioned[0].append(arr[i])
        else:
            partitioned[1].append(arr[i])
    
    return partitioned