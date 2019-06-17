#7. Reverse Integer (Easy)

#Given a 32-bit signed integer, reverse digits of an integer.

#Example 1:
#Input: 123
#Output: 321

#Example 2:
#Input: -123
#Output: -321

#Example 3:
#Input: 120
#Output: 21

#Note:
#Assume we are dealing with an environment which could only store integers within the 32-bit signed integer 
#range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

# Algorithm
#in the while loop : 
	# input: 
	# num = 123
	# rev = 0

	# first interation
	# num = 12
	# rev = 3

	# second iteration
	# num = 1
	# rev = 32

	# third
	# num = 0
	# rev = 321
# check overflow 


class Solution:
    def reverse(self, x: int) -> int:
        # define a reverse integer variable
        rev = 0
        
        #return the absolute value (ignore positive/negative)
        a = abs(x)
        
        # create the movement process 
        while a != 0 :
            # extract the number to move 
            temp = a % 10
            # every time a number moves in the reverse number, it shoud mutiply 10 
            rev = rev * 10 + temp
            # every time a number moves out, the num should divide by 10 
            a = int(a/10)
       
        # check boundary
        # if the number is positive 
        if x > 0 and rev <= 2**31:
            return rev
        # if the number is negative
        elif x < 0 and rev <= 2**31:    # coz it is the absolute number so rev is always positive
            return -rev
        # number is 0 
        else:
            return 0
            
        
            
