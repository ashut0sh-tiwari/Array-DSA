"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""

list1 = [5,6,12,10,25,8,30,16]
target = 20

def twoSum(list, targetnum):
    for i in range(len(list)):
        for j in range(i+1, len(list)): #iterating the list excluding number i
            if list[j] == targetnum - list[i]:
                return [i,j]


solution = twoSum(list1, target)
print(solution)