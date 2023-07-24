def linearBinarySearch(sorted_array, x):
    low = 0
    high = len(sorted_array) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_array[mid] == x:
            return mid
        elif sorted_array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1 #-1 indicate not found

# Example usage:
unsorted_array = [7, 3, 9, 2, 5, 1, 8]
x = 5

# Convert the unsorted array to a sorted array
sorted_array = sorted(unsorted_array)
sorted_array = [1, 2, 3, 5, 7, 8, 9]

# Perform binary search on the sorted array
result = linearBinarySearch(sorted_array, x)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
