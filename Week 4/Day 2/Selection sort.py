def SelectionSort(a,n):
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if a[j]<a[min]:
                min = j
        if min != i:
            temp = a[i]
            a[i] = a[min]
            a[min] = temp
    return a
if __name__ == '__main__':
    a=[5,69,82,46,8,2,95,57]
    print(SelectionSort(a,len(a)))