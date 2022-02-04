#Bubble sort algorithm
def BubbleSort(a,n):
    #Two loops: one for passes, other or swap
    for i in range(n-1):
        flag = 0
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                b = a[j]
                a[j] = a[j+1]
                a[j+1] = b
                flag = 1
        if flag == 0:
            #Break the outer loop if no swap
            #occur in any pass 
            break
    return a

#Driver code
if __name__ == '__main__':
    a=[5,69,82,46,8,2,95,57]
    print(BubbleSort(a,len(a)))