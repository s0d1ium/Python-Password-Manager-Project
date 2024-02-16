def LinearSearch(array, value):
    found = False  # Flag to track if the value is found

    for x in range(len(array)):
        if array[x] == value:
            print(f"Value found at index: {x}")
            found = True  # Update flag to indicate value is found
            break  # Exit loop once the value is found

    if not found:
        print("Value not found")

arr = [2, 5, 8, 10, 11, 15]
LinearSearch(arr, 11)