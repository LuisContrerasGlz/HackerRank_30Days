"""
Given a string, S , of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line.

Note: 0 is considered to be an even index.

Input Format

The first line contains an integer, T  (the number of test cases).
Each line  i of the T subsequent lines contain a string, S.


"""

# Get the number of test cases
num_test_cases = int(input())

# Loop through each test case
for i in range(num_test_cases):
    # Get the string for this test case
    s = input()

    # Initialize empty strings for the even-indexed and odd-indexed characters
    even_chars = ""
    odd_chars = ""

    # Loop through each character in the string
    for j in range(len(s)):
        # If the index is even, add the character to the even_chars string
        if j % 2 == 0:
            even_chars += s[j]
        # If the index is odd, add the character to the odd_chars string
        else:
            odd_chars += s[j]

    # Print the even-indexed and odd-indexed characters, separated by a space
    print(even_chars + " " + odd_chars)
