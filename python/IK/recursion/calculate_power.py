
def calculate_power(a, b):
    """
    Args:
     a(int64)
     b(int64)
    Returns:
     int32
    """
    # Write your code here.
    return power_helper(a , b)

def power_helper(a, b):
    if b == 1 :
        return a 
    if b == 0 :
        return 1
    
    res = power_helper(a, b//2)
    res = res * res
    
    if b % 2 != 0 :
        res = res * a
    return res
result = calculate_power(2, 32)
print(result)