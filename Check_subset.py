# You are given two sets, A and B.
# Your job is to find whether set A is a subset of set B .

# If set A is subset of set B , print True.
# If set A is not a subset of set B, print False.

T = int(input())
for i in range(T):
   
    num_A = int(input())  
    set_A = set(map(int, input().split())) 

    num_B = int(input()) 
    set_B = set(map(int, input().split())) 

    print(set_A.issubset(set_B))
