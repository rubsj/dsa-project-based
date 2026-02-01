
def bubble_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    for i in range(len(arr)-1):
        print(f"i vale is {i}")
        for j in range(len(arr)-1 , i , -1):
            print(f"j vale is {j}")
            if(arr[j]< arr[j-1]):
                (arr[j] , arr[j-1]) = (arr[j-1] , arr[j])
    return arr
result = bubble_sort([64, 34, 25, 12, 22, 11, 90])
print(result)