# Raghu is a shoe shop owner. His shop has X number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are N number of customers who are willing to pay Xi amount of money only if they get the shoe of their desired size.
# Your task is to compute how much money Raghu earned.


from collections import Counter
num_shoes = int(input())
shoe_sizes = list(map(int, input().split()))
inventory = Counter(shoe_sizes)

num_customers = int(input())

total_earnings = 0
for _ in range(num_customers):
    size, price = map(int, input().split())
    if inventory[size] > 0:
        total_earnings += price  
        inventory[size] -= 1    
print(total_earnings)