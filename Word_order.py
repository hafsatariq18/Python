# You are given n words. Some words may repeat. For each word, output its number of 
# occurrences. The output order should correspond with the input order of appearance 
# of the word

N = int(input())
strings = [] 

for i in range(N):
    strings.append(input().strip())  

new = set(strings)
print(len(new))

processed = {}

for i in strings:
    if i in processed:
        processed[i]=processed[i]+1
    else:
        processed[i] = 1

for i in processed:
        print(processed[i],end = ' ')