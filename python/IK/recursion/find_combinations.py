def combinations_recursive(current_number, n, k, current, result):
    print(f"Current Number: {current_number}, Current Combination: {current}")
    if len(current) == k:
        result.append(list(current))
        return
    if current_number == n + 1:
        return

    current.append(current_number)
    combinations_recursive(current_number + 1, n, k, current, result)
    current.pop()
    combinations_recursive(current_number + 1, n, k, current, result)

def find_combinations(n, k):
    result = []
    current = []

    combinations_recursive(1, n, k, current, result)
    return result

result = find_combinations(3, 2)
print(result)