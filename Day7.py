"""

Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Option 1 with reversed function

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    
    for i in reversed(arr):
        print(i, end=" ")

# Option 2

for i in range(len(arr)-1, -1, -1):
    print(arr[i], end=" ")