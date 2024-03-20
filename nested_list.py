if __name__ == '__main__':
    x=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        x.append([name,score])
    lowest_grade = 100000.0
    second_lowest = 100000.0
    for i in x:
      if i[1]< lowest_grade:
        second_lowest = lowest_grade
        lowest_grade = i[1]
      elif lowest_grade <i[1] < second_lowest:
          second_lowest = i[1]
    x.sort()
    for i in x:
       if i[1] == second_lowest:
          print(i[0])
                 