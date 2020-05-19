# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    '''
    If I am given an array: [6, 8, 4, 2, 1, 5, 7]
    I know the computer will initially evaluate the index[0] *6* to be the smallest value
    Then we would want to loop through the rest of the array to find the smallest value out of the range of the array
    Place this at the original index
    Then we will want to change the variable holding the smallest value to be the original index ++
    With that being the new beginning of the loop as we have already found the smallest value
    '''
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(cur_index + 1, len(arr)):
            # I originally attempted to write just an if statement with a cur_index ++ type thing
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        # Your code here
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # i know that the end process of bubble sort is when no swaps where made,
    # then the arr is sorted

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here

    return arr
