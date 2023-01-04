"""

Given a base- 10 integer, n, convert it to binary (base-2). 
Then find and print the base- 10 integer denoting the maximum number of consecutive 1's in n's binary representation. 
When working with different bases, it is common to show the base as a subscript.

"""

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    def max_consecutive_ones(n):
        binary = bin(n)[2:] # strip the '0b' prefix
        max_count = 0
        current_count = 0
        for bit in binary:
            if bit == '1':
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
        return max_count

print(max_consecutive_ones(n))