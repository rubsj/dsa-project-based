
from build_a_bst import build_a_bst , serialize_leetcode


def delete_from_bst(root, values_to_be_deleted):
    """
    Args:
     root(BinaryTreeNode_int32)
     values_to_be_deleted(list_int32)
    Returns:
     BinaryTreeNode_int32
    """
    # Write your code here.
    for val in values_to_be_deleted :
        if root is None :
            return None
        root = delete(root , val)
    return root

def delete(root , val):

    # search the node
    curr = root
    prev = None
    
    while curr is not None:
        if curr.value == val:
            break
        elif val < curr.value :
            prev = curr
            curr = curr.left
        else :
            prev = curr
            curr = curr.right
    # if value is not found in tree , curr will be None
    if curr is None :
        return root
        
    # if found node is leaf
    if curr.left is None and curr.right is None :
        # if the node to be deleted is the only node is tree return None
        if prev is None :
            return None
        if prev.left == curr :
            prev.left = None
        else :
            prev.right = None
    
    # if node has one child 
    elif curr.left is None and curr.right is not None :
        if prev is None : 
            root = curr.right
            return root
        if prev.left == curr:
            prev.left = curr.right
        else:
            prev.right = curr.right
    elif curr.right is None and curr.left is not None :
        if prev is None:
            root = curr.left
            return root
        if prev.left == curr:
            prev.left = curr.left
        else :
            prev.right = curr.left
        return root
        
    else:
        # if the node has both the child
        # find the successsor of the current node
        prev_succ = curr
        succ = curr.right
        while succ.left is not None :
            prev_succ = succ
            succ = succ.left
            
        #set successor value to current nodes value
        curr.value = succ.value
        
        # delete the successor , it can have only right child or no child
        if succ == prev_succ.left :
            prev_succ.left = succ.right
        else:
            prev_succ.right = succ.right
    return root
"""
{
"root": [4,
2, 6,
1, 3, 5, 7],
"values_to_be_deleted": [5, 6]
}

"""
#result = delete_from_bst(build_a_bst([4,2, 6,1, 3, 5, 7]) , [5, 6])
#print(serialize_leetcode(result))

"""

{
"root": [120,
100, 200,
-1000000000, null, null, 1000000000],
"values_to_be_deleted": [1000000000, 100, 120]
}
"""
root =build_a_bst([120, 100, 200,-1000000000, None, None, 1000000000])
result = delete_from_bst(root , [1000000000, 100, 120])
print(serialize_leetcode(result))