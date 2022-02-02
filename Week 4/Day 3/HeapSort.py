def MaxHeapify(arr,n,i):
	larger = i
	l = 2*i
	r = 2*i+1
	if(l<=n and arr[l]>arr[larger]):
		larger = l
		

	if(r<=n and arr[r]>arr[larger]):
		larger = r

	if (larger!=i):
		swap(arr[larger],arr[i])
		MaxHeapify(arr,n,larger)

	return arr

def HeapSort(a,n):
	for i in range(n//2,1,-1):
		#print(i)
		MaxHeapify(a,n,i-1)
	for i in range(n,1,-1):
		swap(a[1],a[i-1])
		arr = MaxHeapify(a,n,1)

	return arr

def swap(b1,b2):
	temp = b1
	b1 = b2
	b2 = temp
if __name__ == '__main__':
	a=[15,5,20,1,17,10,30]
	HeapSort(a,len(a))