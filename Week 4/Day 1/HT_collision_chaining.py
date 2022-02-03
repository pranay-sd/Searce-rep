class HashTable:
    def __init__(self):
        self.Max = 10
        #now we are storing key value pair, so each
        #element of array will be an array, which will
        # store the tuples of key-value pairs
        self.arr = [[] for i in range(self.Max)]

    def get_hash(self, key):
        #calculating hash value
        h = 0
        for char in key :
            h += ord(char)
        return h % self.Max

    def __setitem__(self, key, value) :
        hash = self.get_hash(key)
        
        found = False
        #Iterating through the Linked list to check whether 
        #the key already exists and if so, update the value
        #for the key 
        for idx, element in enumerate(self.arr[hash]):
            if len(element) == 2 and element[0] == key:
                #Modify the key-value pair 
                self.arr[hash][idx] = (key, value)
                found = True

        #If key does not exist, directly append a new
        #key-value pair
        if not found:
            self.arr[hash].append((key,value))
        

    def __getitem__(self, key) :
        hash = self.get_hash(key)
        for ele in self.arr[hash] :
            if ele[0] == key :
                return ele[1]

    def __delitem__(self, key):
        hash = self.get_hash(key)
        for idx, ele in enumerate(self.arr[hash]) :
            if ele[0] == key :
                del self.arr[hash][idx]

if __name__== '__main__':
    t = HashTable()
    t['mar-4'] = 12
    t['mar-7'] = 17
    t['mar-8'] = 16
    t['mar-15'] = 15
    t['mar-16'] = 19
    t['mar-17'] = 14
    t['mar-18'] = 13
    print(t.arr)
    t['mar-4'] = 15
    print('\n')
    print(t.arr)

#mar-4,15