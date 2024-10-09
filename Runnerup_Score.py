# Given the participants' score sheet for your University Sports Day, 
# you are required to find the runner-up score. You are given n scores. 
# Store them in a list and find the score of the runner-up.


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    winner =-120
    runnerup =120
    
    for i in arr:
        if i > winner:
          runnerup = winner
          winner = i
        elif i<winner and i>runnerup:
          runnerup = i
    print(runnerup)
        