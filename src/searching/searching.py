def linear_search(arr, target):
    # Your code here
    # moves sequentintially
    # so I automatically think of going through the loop
    # if I have not found the target yet
    # once we do find the target return it
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    found = None
    # Compare the item in the middle of the data set to the item we are searching for.
    middle_index = len(arr) // 2

    while target is not found:
        # If it is the same, stop. We found it and are done!
        if target == arr[middle_index]:
            found = arr[middle_index]
            return middle_index
        # Else, if the item we are searching for is LESS than the item in the middle:
        elif target < arr[middle_index]:
            # Eliminate the RHS of list. Repeat step 1 with only the LHS of list.
            middle_index = middle_index // 2
        # Else, the item we are searching for is GREATER than the item in the middle:
            # Eliminate the LHS of list. Repeat step 1 with only the RHS of the list
        elif target > arr[middle_index]:
            pass
    return -1  # not found
