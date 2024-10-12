# Ms. Gabriel Williams is a botany professor at District College. 
# One day, she asked her student Mickey to compute the average of all the plants with 
# distinct heights in her greenhouse.

def average(array):
    # your code goes here
   elements = set(array)
   result = sum(elements)/len(elements)
   return result
if __name__ == '__main__':