
"""You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits."""


list = [2,4]

#slow function because of type convertion
def plusOne(list):
    num = 0
    for i in range(len(list)): #looping
        num += list[i] * pow(10, len(list)-1-i) #adding number to the num with their tens position
    return [int(i) for i in str(num+1)] #converting into str into int

#fast function
def plusOne2(list):
    for i in range(len(list)-1,-1,-1): #range function takes three arguement (starting index, end index +1, steps )
        if list[i] == 9:
            list[i] = 0
        else:
            list[i]+=1
            return[list]
    return [1] + list

res = plusOne2(list)
print(res)



