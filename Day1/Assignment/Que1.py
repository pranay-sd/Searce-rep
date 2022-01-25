def reverseArray(a):
    b= list()
    
    for i in range(len(a)):
        b.append(a[len(a)-i-1])
    return b

if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)
    print(res)