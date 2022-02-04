#Insertion sort algorithm
def InsertionSort(a,n):
    #loop starts from index '1', as 1st element
    #is already in sorted array
    for i in range(1,n):
        temp = a[i]
        j = i-1

        #loop to add ith element from unsorted 
        #array to sorted at suitable position 
        while j>=0 and a[j]>temp:
            a[j+1] = a[j]
            j-=1

        a[j+1] = temp
    return a

#Driver code
if __name__ == '__main__':
    a=[5,69,82,46,8,2,95,57]
    print(InsertionSort(a,len(a)))