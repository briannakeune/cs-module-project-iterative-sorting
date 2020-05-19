
# assuming the arr is sorted

# returns the index of the target if it exists in the arr
# otherwise, returns -1
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
    return - 1


# insertion sort

# [6, 5, 3, 1, 8, 7, 2, 4]

# this is the sorting algo that seperates each index into it's own array
# and then adds them together while sorting?
# like two seperated arrays
# do we hold them like a temp array?

# [6, 5] [3, 1, 8, 7, 2, 4]
# sort first arr
# [5, 6] [3, 1, 8, 7, 2, 4]
# [5, 6, 3] [1, 8, 7, 2, 4]
# etc

'''
Conceptualize a sorted half and an unsorted half
Initially the sorted half consists of just the first element
Iterate along the rest of the array
Place it in its appropriate spot in the sorted half
The sorted half grows until it encompasses the entire array
Until there is nothing left that is unsorted
'''


class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre


def insertion_sort_books(arr_of_books):
    # what are we sorting by, author...
    for i in range(1, len(arr_of_books)):
        # the 1 ^ is there because we are seperating what is already sorted
        curr_book = arr_of_books[i]
        j = i
        # put current book in the appropriate spot in our sorted half
        # loop through sorted half and find the appropriate spot
        while j > 0 and curr_book.author < arr_of_books[j - 1].author:
            # taking the j - 1th book and copying it over to the jth spot
            arr_of_books[j] = arr_of_books[j - 1]
            j -= 1
        # insert the book at the correct position
        arr_of_books[j] = curr_book
