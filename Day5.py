"""
Given an integer, n , print its first 10 multiples. 
Each multiple nxi (where ) i should be printed on a new line in the form: n x i = result.

"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    iteracion = 1 
    while iteracion <= 10:
        resultado = iteracion * n
        print (f"{n} x {iteracion} = {resultado}")
        # print (resultado)
        iteracion += 1