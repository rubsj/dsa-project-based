def get_permutations(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    result = []
    permutation_helper(arr, [] , result)
    return result
    
def permutation_helper(arr , current , result):
    if len(arr) == 0 :
        return result.append(current)
    else:
        for i in range(len(arr)):
            permutation_helper(arr[:i] + arr[i+1:] , current + [arr[i]] , result)
            
result = get_permutations([1,2,3])
print(result)