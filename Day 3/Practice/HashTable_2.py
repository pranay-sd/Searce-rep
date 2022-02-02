#Implementing HashTable by creating a hash function
#using OOP.

class HashTable :
    def __init__(self):
        self.Max = 50
        self.array = [None for i in range(self.Max)]
        #alloted some memory to the hashtable

    def get_hash(self, key):
        #calculating hash value
        h = 0
        for char in key :
            h += ord(char)
        return h % self.Max

    #Adding new element 
    def add(self, key, value) :
        hash = self.get_hash(key)
        self.array[hash] = value

    #Retrival of an element/value given its key
    def get(self, key) :
        hash = self.get_hash(key)
        return self.array[hash]

#Driver code

if __name__ == "__main__" :
    HT= HashTable()
    
    HT.add('XUV500', "15-20 lacs")
    HT.add('XUV700', "13-20 lacs")
    HT.add('XUV300', "8-13 lacs")
    #HT['XUV500'] = 15-20 lacs
    print(HT.get('XUV500'))