# febunachi

def febunachi(n):
    if n == 0 or n == 1:
        return n
    return febunachi(n-1) + febunachi(n-2)


print(febunachi(6))