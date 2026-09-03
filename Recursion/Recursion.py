
def printNumbrs(i,n):
    if i > n :
        return
    print(i,end=" ")
    printNumbrs(i+1, n)
    print(i)

printNumbrs(1,7)
