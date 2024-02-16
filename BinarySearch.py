def binary_search(arr, target, low, high):
    if low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid
        elif mid_value < target:
            return binary_search(arr, target, mid + 1, high)
        else:
            return binary_search(arr, target, low, mid - 1)
    else:
        return -1

# Example usage
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 10

result = binary_search(array, target_value, 0, len(array) - 1)

if result != -1:
    print(f'Target {target_value} found at index {result}.')
else:
    print(f'Target {target_value} not found in the array.')