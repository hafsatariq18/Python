# Given an integer,n,print the following values for each integer  
# from 1 to n:

# 1.Decimal
# 2.Octal
# 3.Hexadecimal (capitalized)
# 4.Binary

def print_formatted(number):
    # your code goes here
    width = len(bin(number)) - 2  
    for i in range(1, number + 1):
     
        print("{0:>{width}d} {0:>{width}o} {0:>{width}X} {0:>{width}b}".format(i, width=width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)