# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be N X M. (N is an odd natural number, and M is 3 times N.)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.

X = ".|."
N, M = map(int, input().split()) 
pattern = "-"
half = (M-3)//2
for i in range (half+1):
  print((half*pattern)+ X + (half*pattern))
  half = half - 3
  X = ".|." * (2 * i + 3)
  if half <3:
    break
H =(M - 7)//2
print((H*pattern)+ "WELCOME" + (H*pattern))

half = 3  
for i in range((N-1)//2, 0, -1):  
    X = ".|." * (2 * i - 1) 
    print((half * pattern) + X + (half * pattern)) 
    half += 3 