# Write a Python program that takes a list of integers as input and returns the second largest number 
# in the list. If the list has fewer than 2 unique numbers, the program should return None.


def find_second_largest(numbers):
    unique_numbers = sorted(set(numbers), reverse=True)
   
    if len(unique_numbers) >= 2:
        return unique_numbers[1]
    else:
        return None

if __name__ == "__main__":
    user_input = input("Enter a list of numbers separated by spaces: ")
  
    numbers = list(map(int, user_input.split()))
    
    second_largest = find_second_largest(numbers)
    
    if second_largest is not None:
        print("The second largest number is:", second_largest)
    else:
        print("There is no second largest number.")