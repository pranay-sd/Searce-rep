def InsertionSort(a,n):
    for i in range(1,n):
        temp = a[i]
        j = i-1
        while j>=0 and a[j]>temp:
            a[j+1] = a[j]
            j-=1
        a[j+1] = temp
    return a

if __name__ == '__main__':
    a=[5,69,82,46,8,2,95,57]
    print(InsertionSort(a,len(a)))