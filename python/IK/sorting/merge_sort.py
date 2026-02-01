
def merge_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    if len(arr) <=1 :
        return arr
    merge_sort_internal(arr , 0 , len(arr)-1)
    return arr


def merge_sort_internal(arr , start , end):
    if start >= end :
        return 
    mid = start + (end - start)//2
    merge_sort_internal(arr , start , mid)
    merge_sort_internal(arr , mid +1 , end)
    merge(arr , start , mid , end)
    
    
def merge (arr , start , mid , end):
    #tbd
    left_start = start
    left_end = mid
    right_start = mid +1
    right_end = end
    aux_arr = [0] * (end - start +1)
    aux_index = 0
    
    while left_start <= left_end and right_start <= right_end:
        if arr[left_start] < arr[right_start] :
            aux_arr[aux_index] = arr[left_start]
            left_start = left_start + 1
        else :
            aux_arr[aux_index] = arr[right_start]
            right_start =  right_start +1
        aux_index = aux_index + 1
        
    while left_start <= left_end :
        aux_arr[aux_index] = arr[left_start]
        left_start = left_start + 1
        aux_index = aux_index + 1
    
    while right_start <= right_end:
        aux_arr[aux_index] = arr[right_start]
        right_start =  right_start +1
        aux_index = aux_index + 1
            
    for i in range(len(aux_arr)):
        arr[start + i] = aux_arr[i]
        
result = merge_sort([5, 8, 3, 9, 4, 1, 7])
print(result)