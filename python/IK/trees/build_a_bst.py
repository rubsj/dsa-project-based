
from collections import deque


def serialize_leetcode(root):
    """
    Serializes a binary tree to LeetCode's exact format.
    Example: [1,2,null,3]
    """
    if root is None:
        return "[]"

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()

        if node is None:
            result.append("null")
        else:
            result.append(str(node.value))
            queue.append(node.left)
            queue.append(node.right)

    # 🔴 Trim trailing "null"s (LeetCode requirement)
    while result and result[-1] == "null":
        result.pop()

    return "[" + ",".join(result) + "]"

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def build_a_bst(values):
    """
    Args:
     values(list_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.
    root = None
    for k in values :
        if k is None :
            continue
        root = insert_bst(k , root)
    
    return root


def insert_bst(key, root):
    if root is None : 
        return BinaryTreeNode(key)
        
    prev = None
    curr = root
    while curr is not None :
        if key == curr.value :
            return curr
        elif key < curr.value :
            prev = curr
            curr = curr.left
        else :
            prev = curr
            curr = curr.right
    if key < prev.value :
        prev.left = BinaryTreeNode(key)
    else:
        prev.right = BinaryTreeNode(key)
    return root
    
"""    
input = [5, 8, 3, 9, 4, 1, 7]  

result = build_a_bst(input)
print(serialize_leetcode(result))

input =  [-10000, 10000]
result = build_a_bst(input)
print(serialize_leetcode(result))
"""