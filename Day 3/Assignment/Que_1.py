from heapq import heappop, heappush

def minAvg(customers):
    t_total = t_wait = 0
    #sorting customer based on their arrival time
    #in reverse order so when we pop any element it wouuld take O(1)
    customers.sort(reverse = True)
    queue = []

    while customers or queue:
        #Only those cusomers can be served who have arrived
        #and their shuld be customers left to be served
        while customers and customers[-1][0] < t_total :
            heappush(queue, customers.pop()[::-1])
        if queue:
            t_cook = heappop(queue)
            t_total += t_cook[0]
            t_wait += t_total - t_cook[1]
        else :
            heappush(queue, customers.pop()[::-1])
            t_total = queue[0][1]

    return t_wait // N

if __name__ == '__main__':

    N = int(input("Number of customers : "))

    customers = []
    for i in range(N) :
        customers.append(list(map(int, input().rstrip().split())))

    print(minAvg(customers))
