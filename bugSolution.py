def function_with_uncommon_error(a, b):
    if a == 0:
        return float('inf') # Handle zero division
    return a + b

result = function_with_uncommon_error(0, 10)
print(result)  # Output: inf 