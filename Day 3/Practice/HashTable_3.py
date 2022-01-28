 #Simplifying the access of values just like a dictionery
class HashTable:
    def __init__(self):
        self.Max = 50
        self.array = [None for i in range(self.Max)]

    def get_hash(self, key):
        h = 0
        for char in key :
            h += ord(char)
        return h % self.Max

    def __setitem__(self, key, value) :
        hash = self.get_hash(key)
        self.array[hash] = value

    def __getitem__(self, key) :
        hash = self.get_hash(key)
        return self.array[hash]

#Driver code

if __name__ == "__main__" :
    HT= HashTable()
    HT['XUV500'] = "15-20 lacs"
    HT['XUV700'] = "13-20 lacs"
    HT['XUV300'] = "8-13 lacs"
    #HT['XUV500'] = 15-20 lacs
    print(HT['XUV500'])



