'''
13. Roman to Integer (Easy)
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

'''

class Solution:
	def romanToInt(self, s) ->int :
	'''
    type of s : string
    rtype: int
	'''

    # define the dictionary for later use 
    numeric_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    # initiate the result
    result = 0

    # loop through the whole string: 
    # two case: numeric_map[ s[left] ] < numeric_map[ s[right] ], temp = numeric_map[ s[right]] - numeric_map[s[left] ], result += temp 
    #           numeric_map[ s[left] ] > numeric_map[ s[right] ],  result += numeric_map[ s[right] ]
    # compare the values not just keys, so s[left] and s[right]
    
    for i in range(len(s)):
    	# i must greater than 0 , then i-1 can exist
        if i > 0 and numeric_map[ s[i] ] > numeric_map[ s[i-1] ]:
        	# mutiple 2 
            temp =  numeric_map[ s[i] ] - 2 * numeric_map[ s[i-1] ]
            result += temp 
        else:
            result += numeric_map[ s[i] ]
    return result   

# for example Input: "MCMXCIV"
# M is 1000, C is 100 , X is 10 
# first 3 letters, M + C + (M-C) = M+M. But the result should be M + C + M . To ahcieve this, we change it to M + C + 2 * (M-C)

