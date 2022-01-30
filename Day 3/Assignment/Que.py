#To find next customer to be served: the one who arrived on or 
#before present time and has minimum time required to cook pan
def next_cust(arr, Tn):
    l = len(arr)
    min = arr[0][1]
    b = arr[0][0]
        
    for i in range(l):
        if arr[i][1] < min and arr[i][0]<=Tn:
            min = arr[i][1]
            b = arr[i][0]
    return arr.index([b,min])

#To find minimum average time
def min_avg_wtime(data, total_cust) :
    #Variables to track the present time update wait times for customers
    Tnow = 0 
    Twaitsum = 0 
    #print(data)
    #Total loops will be equal to number of customers
    for i in range(total_cust) : 
            
        #1st customer: The one with arrival time = 0
        if i == 0:
            for k in range(total_cust):
                if data[k][0] == 0:
                    #print(data[k][0])
                    j = k
                    break
         
        #last customer
        elif i == total_cust-1:
            j = 0

        #For any other customer
        else :
            j = next_cust(data, Tnow)
            
        #Adding the wait times and updating present time
        Tnow += int(data[j][1]) 
        Twaitsum += (Tnow-data[j][0])

        #Remove the customer from the list who is served 
        data.remove(data[j])

    # Return the average wait time
    return Twaitsum//total_cust

if __name__ == "__main__":

    N = int(input("Number of customers : "))
    cust_arr = []
    for i in range(N):
        cust_arr.append(list(map(int, input().rstrip().split())))

    print(min_avg_wtime(cust_arr, N))