# You are given a set A and N number of other sets. These  number of sets have to perform some specific mutation operations on set A .
# Your task is to execute those operations and print the sum of elements from set A.

n = int(input())
set_A = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    operation_data = input().split()
    operation_name = operation_data[0]  
    length_of_other_set = int(operation_data[1])  

    other_set = set(map(int, input().split()))
    if operation_name == "intersection_update":
        set_A.intersection_update(other_set)
    elif operation_name == "update":
        set_A.update(other_set)
    elif operation_name == "symmetric_difference_update":
        set_A.symmetric_difference_update(other_set)
    elif operation_name == "difference_update":
        set_A.difference_update(other_set)
print(sum(set_A))