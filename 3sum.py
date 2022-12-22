"""Given an integer array list, return all the triplets [list[i], list[j], list[k]] such that i != j, i != k, and j != k, and list[i] + list[j] + list[k] == 0.

Notice that the solution set must not contain duplicate triplets."""

nums = [-1,0,1,2,-1,-4]

def threeSum(list):
        res = [] #initialising an empty list
        list.sort() #sorting the input list

        for i,a in enumerate(list): #looping the list with enumerate function to get the index value as well
            if i >0 and a == list[i-1]: # if not the starting index and the value of its previous index is equal then skipping that index
                continue
            l = i + 1 #initialising the variable
            r = len(list)-1 #initialising the variable
            while l<r: #using while loop until l and r are not same
                threesum = a + list[l] + list[r] #initialising the sum variable
                if threesum > 0: #if sum is greater than 0 then decrementing the r variable
                    r-=1
                elif threesum <0: #if sum is less than 0 then incrementing the l variable
                    l +=1
                else:
                    res.append([a,list[l],list[r]]) #if sum is equal to 0 then appendind these number in the res
                    l+=1 # incrementing l variable
                    while list[l]==list[l-1] and l<r: #using while loop to increment l until with condition in which l and its previous value is not same and l<r
                        l+=1 
        return res #returning res

solution = threeSum(nums)
print(solution)