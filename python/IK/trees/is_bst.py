
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def is_bst(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     bool
    """
    # Write your code here.
    NEG_INF = float("-inf")
    POS_INF = float("inf")
    return dfs(root, NEG_INF , POS_INF)


def dfs(root, low , high):
    if root is None : 
        return True
        
    val = root.value
        
    if (val < low) or (val > high):
        return False
        
    left_ok = dfs(root.left, low , val)
    right_ok = dfs(root.right, val , high)

    return left_ok and right_ok        
        
def is_bst_2(root):
    def dfs(node, low, high):
        if node is None:
            return True

        v = node.value
        if low is not None and v < low:
            return False
        if high is not None and v > high:
            return False

        if not dfs(node.left, low, v):
            return False
        if not dfs(node.right, v, high):
            return False

        return True

    return dfs(root, None, None)