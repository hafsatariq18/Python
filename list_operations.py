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