"""
Given two strings str1 and str2, find the indices in str1 that can be removed to make str1 equal to str2.
If it's not possible to make str1 equal to str2 by removing characters, return an empty list.
"""

def find_removable_indices(str1, str2):
    # If str2 is longer than str1, it's impossible to make them equal
    if len(str2) > len(str1):
        return []
    
    # If strings are already equal, no indices need to be removed
    if str1 == str2:
        return []
    
    removable_indices = []
    i = 0  # pointer for str1
    j = 0  # pointer for str2
    
    # Iterate through str1
    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            # Characters match, move both pointers
            i += 1
            j += 1
        else:
            # Characters don't match, mark current index as removable
            removable_indices.append(i)
            i += 1
    
    # If we've reached the end of str2 and str1 has remaining characters
    while i < len(str1):
        removable_indices.append(i)
        i += 1
    
    # Check if removing the indices makes str1 equal to str2
    result = ''.join(char for i, char in enumerate(str1) if i not in removable_indices)
    if result == str2:
        return removable_indices
    return []

if __name__ == "__main__":
    # Get input strings
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    
    # Find removable indices
    indices = find_removable_indices(str1, str2)
    
    # Print result
    if indices:
        print("Indices to remove:", indices)
    else:
        print("Cannot make the strings equal by removing characters") 