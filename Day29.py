"""

Given an array, a, of size n distinct elements, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following  lines:

Array is sorted in numSwaps swaps.
where numSwaps is the number of swaps that took place.
First Element: firstElement
where  firstElement is the first element in the sorted array.
Last Element: lastElement
where  lastElement is the last element in the sorted array.
Hint: To complete this challenge, you will need to add a variable that keeps a running tally of all swaps that occur during execution.

"""

#!/bin/python3

import math
import os
import random
import re
import sys


def bubble_sort(a):
    num_swaps = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                num_swaps += 1
    return num_swaps


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    num_swaps = bubble_sort(a)
    print("Array is sorted in {} swaps.".format(num_swaps))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))
