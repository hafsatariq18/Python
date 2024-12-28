# You are given a string S. It consists of alphanumeric characters, spaces and symbols(+,-).
# Your task is to find all the substrings of S that contains 2 or more vowels.
# Also, these substrings must lie in between 2 consonants and should contain vowels only.

S = input()
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

result = []  
current_vowels = "" 


for i in range(len(S)):
    if S[i] in vowels:  
        current_vowels += S[i]  
    else:
        
        if len(current_vowels) >= 2 and i > 0 and S[i - len(current_vowels) - 1] in consonants:
            result.append(current_vowels)
        current_vowels = ""  

if len(current_vowels) >= 2 and len(S) > len(current_vowels) and S[len(S) - len(current_vowels) - 2] in consonants:
    result.append(current_vowels)

if result:
    for seq in result:
        print(seq)
else:
    print(-1)