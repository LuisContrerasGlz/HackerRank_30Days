"""

Given a 6x6  2D Array, A: 
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0

We define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation:

a b c
  d
e f g

There are  16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.
Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.


"""

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    max_sum = -float('inf')  # Initialize max sum to a very low value

    for i in range(len(arr) - 2):  # Iterate through rows of the array
        for j in range(len(arr[i]) - 2):  # Iterate through columns of the array
            # Sum the values of the hourglass pattern
            hourglass_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + \
                arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

            # Update max sum if hourglass sum is greater
            max_sum = max(max_sum, hourglass_sum)

    print(max_sum)  # Print the maximum hourglass sum
