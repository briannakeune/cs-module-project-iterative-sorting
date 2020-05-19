Determining time complexity:

1. Compute the big O of each line in isolation.
2. If something is in a loop, multiply it's big O by the number of iterations of the loop.
3. If two things happen sequentially, add the big 0s.
4. Drop the leading multiplicative constants from each big O.
5. From all of the big os that are added, drop all but the biggest, dominating one.

Space (or memory) complexity measure how much _additional_ memory an algorithm allocates in order to run.

One big giveaway that an algorithm is utilizing additional memory is if it initializes a data structure.

We use the same big O notation when talking about space complexity.

Just like with time complexity, space complexity is concerned with the worse case.


# O(n^2) time, O(n^2) space
def o_n2_space(n):
    times_table = []

    for i in range(n):
        row = []

        for j in range(n):
            row.append(j * i)

        times_table.append(row)

    return times_table

when data is sorted, it is easier/more effiencnt to search through.
sorted - a method/rules when data is inserted.


# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] - already ordered/sorted
