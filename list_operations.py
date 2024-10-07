# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines
# of commands where each command will be of the 7 types listed above. 
# Iterate through each command in order and perform the corresponding operation on your list.

if __name__ == '__main__':
    N = int(input())
    l = []

    for _ in range(N):
        values = input().split(' ')

        if values[0] == "insert":
            l.insert(int(values[1]), int(values[2]))
        elif values[0] == "append":
            l.append(int(values[1]))
        elif values[0] == "remove":
            l.remove(int(values[1]))
        elif values[0] =="print":
            print(l)
        elif values[0] == "sort":
            l.sort()
        elif values[0] == "pop":
            l.pop()
        elif values[0] == "reverse":
            l.reverse()