# You are given a space separated list of integers. If all the integers are positive, 
# then you need to check if any integer is a palindromic integer.

# Input Format

# The first line contains an integer N. N is the total number of integers in the list.
# The second line contains the space separated list of N integers

N = int(input())
numbers = list(map(int, input().split()))

all_positive = all(num > 0 for num in numbers) > 0 
any_palindromic = any(str(num) == str(num)[::-1] for num in numbers)

print (all_positive and any_palindromic)