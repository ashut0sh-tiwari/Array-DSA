"""Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing."""

class MyHashSet: #class hashset

    def __init__(self): #contructor function
        self.size = 10000 #initialising the size 
        self.table = [None]*self.size #creating an array of size with None values

    def add(self, key): #function to add element
        hv = self.calculate(key) #first get the hash value 
        if self.table[hv] == None: #if there is none value at that position then assign that position to key 
            self.table[hv] = [key]
        else:
            self.table[hv].append(key) #if position is not empty then append that element into bucket(list) at that position
        

    def remove(self, key): #function to remove element
        hv = self.calculate(key) #first get the hash value 
        if self.table[hv]!=None: #if position is not empty then iterate over the bucket(list) at that positionand remove every element which contains the key
            while key in self.table[hv]:
                self.table[hv].remove(key)
        

    def contains(self, key): #function to check if list contains the element or not
        hv = self.calculate(key) #first get the hash value 
        if self.table[hv] != None: #if position is not empty then return key at that position
            return key in self.table[hv]
        return False #else return false
        
    def calculate(self, key): #function to get the hash value 
        return key % self.size #using mod operator