"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space."""

nums = [4,1,2,1,2]

"""In Python, XOR is a bitwise operator that is also known as Exclusive OR. It is a logical operator which outputs 1 when either of the operands is 1 (one is 1 and the other one is 0), but both are not 1, and both are not 0. The symbol for XOR in Python is '^' and in mathematics, its symbol is '⊕'."""

def singleNumber(nums): #function to find unique number form the array
        res = 0 #initialising the variable
        for i in nums: #looping through the array
            res = i ^ res #using xor bitwise operator to evaluate elements with each other same number will give output 0 and unique number will give 1 but in this case unique number will be stored in the variable      
        return res #returning the output

solution = singleNumber(nums)
print(solution)