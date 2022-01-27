#Implementing HashTable by creating a hash function
#using OOP.

class HashTable :
    def __init__(self):
        self.Max = 50
        self.array = [None for i in range(self.Max)]

    def get_hash(self, key):
        h = 0
        for char in key :
            h += ord(char)
        return h % self.Max

    def add(self, key, value) :
        hash = self.get_hash(key)
        self.array[hash] = value

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