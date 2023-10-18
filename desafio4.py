if __name__ == '__main__':
    n = int(input())
    a = 0;
    for i in range(1, n+1):
            if (i > 99):
                a = a*1000 + i
            elif (i > 9):
                a = a*100 + i
            else:
                a = a*10 + i
        
print(a)