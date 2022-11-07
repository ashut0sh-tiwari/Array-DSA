"""Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory."""

l1 = [1,2,2,3,4,5,6,6,7,8,9,9,9]

def lengthOfList(list): #total number of elements after removing duplicates items from the list
    j = 0 #initializing the variable
    for i in range(1, len(list)): #iterating through the list with index +1
        print('-')
        print(list[j])
        print(list[i])
        print('-')
        if list[j] != list[i]: 
            j += 1 #incrementing the variable for unique elements
            list[j] = list[i] #updating the variable value
            print('-')
            print(list[j])
            print(list[i])
            print('-')
    return j+1 #returning + 1 because we started from 0 index

solution = lengthOfList(l1)
print(solution)
