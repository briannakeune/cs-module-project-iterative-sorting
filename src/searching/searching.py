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
    # *how to find the midpoint*
    # let's figure out the total size of the arr
    left = 0
    right = len(arr) - 1
    # find the midpoint

    while left <= right:
        mid = (left + right) // 2

        # check to see if the midpoint elemnet is our target
        if arr[mid] == target:
            return mid

        # check to determine which side the element should be placed
        if arr[mid] < target:
            # toss out of the left side of the arr
            left = mid + 1
       # otherwise, arr[mid] > target
        else:
            # toss out the right side
            right = mid - 1
    return -1  # not found
