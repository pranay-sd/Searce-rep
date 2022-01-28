class AvgTime :
    def __init__(self) :
        pass

    #To find wait time of a customer
    def wait_time(self, Tarrival, Tcook, Tstart):
        return int(Tstart)+int(Tcook)-int(Tarrival)

    #To find next customer to be served
    def next_cust(self, arr, Tn):
        l = len(arr)
        min = arr[0][1]
        b = arr[0][0]
        for i in range(l):
            if arr[i][1] < min and arr[i][0]<=Tn:
                min = arr[i][1]
                b = arr[i][0]
        return arr.index([b,min])

    #To find minimum average time
    def min_avg_wtime(self, data, total_cust) :
        Tnow = 0
        Tsum = 0
        #print(data)
        for i in range(total_cust) :
            
            #1st customer
            if i == 0:
                for k in range(total_cust):
                    if data[k][0] == 0:
                        #print(data[k][0])
                        j = k
                        break
                    else :
                        continue
         
            #last customer
            elif i == total_cust-1:
                j = 0

            #any other customer
            else :
                j = self.next_cust(data, Tnow)
            T = self.wait_time(data[j][0], data[j][1], Tnow)
            Tsum += T
            Tnow += int(data[j][1])
            data.remove(data[j])

        return Tsum/total_cust
        
    pass


if __name__ == "__main__":

    N = int(input("Number of customers : "))
    
    avg = AvgTime()

    cust_arr = []
    for i in range(N):
        cust_arr.append(list(map(int, input().rstrip().split())))
        #cust_arr.append(input().rstrip().split())
    
    print(avg.min_avg_wtime(cust_arr, N))