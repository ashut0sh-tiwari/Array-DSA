"""Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array."""

l1 = [1,2,3,0,6,4,7,5]

#function to find the missing value in the list
def listSum(list):
    #initialising the variable
    res = len(list)
    for i in range(len(list)):
        print('-')
        print(list[i])
        print('-')
        #adding the length of the list and minimise list index value with every iteration 
        res += (i-list[i])
        print('-')
        print(res)
        print('-')

def listSum2(list): #function to find the missing value in the list
    n = len(list)+1 #initialising the variable with total number of elements including 0
    sum_ = n*(n-1)//2 #sum of n number of values
    return sum_ - sum(list) #returning output after substracting sum of values in the list from sum of n values



solution = listSum2(l1)
print(solution)