# You are given a string S and width w .
# Your task is to wrap the string into a paragraph of width w.

# Function Description

# Complete the wrap function in the editor below.

# wrap has the following parameters:

# string string: a long string
# int max_width: the width to wrap to

import textwrap

def wrap(string, max_width):
    filled_text = textwrap.fill(string, max_width)
    return (filled_text)
 
if __name__ == '__main__':