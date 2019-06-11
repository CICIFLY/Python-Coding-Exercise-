
#3.Given a string, find the length of the longest substring without repeating characters. ( medium)

#Example 3:

#Input: "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3. 
#             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

#Solution: use map to track the string length 

class Solution:
    def lengthOfLongestSubstring(self, s):
    	"""
        type s : string
        rtype: int
    	"""
    	# dict is reserved word so change it to dicts. 
    	# characters as keys, indices as values (to calculate length we will need the indices of start and the repeated character)
        # when we find a repeated chracter, the start point should be updated
        # maxlength also need to be updated when a new length occurs


        # solution 1
        start = -1
        # start from -1 because max = i - start, considering there is only 1 character in the string , maxlength  = 0-(-1)
        maxlength = 0
        dicts = {}

        for i in range(len(s)):
        	# character s[i] in the dict already 
        	if s[i] in dicts and dicts[s[i]] > start:
        		# update start point
        		start = dicts[s[i]]
        		# write the character into dictionary 
        		dicts[s[i]] = i 

        	# character is not in the dictionary yet
        	else:
        		# write the character into dictionary 
        		dicts[s[i]] = i 
        		# compare lengths 
        		if i - start > maxlength:
        			maxlength = i - start
        return maxlength 



        # solution 2 
    	dicts = {}   
    	maxlength = start = 0
    	for idx, value in enumerate(s):

    		# character in the dictionary already, update start point 
    		if value in dicts:
    			sums = dicts[value] +1  
    			if sums > start:
    				start = sums

    		# character not in dictionary yet, calculate the length(num) 
    		num = idx - start + 1 
            if num > maxlength:
            	maxlength = num
            
            # write the character and index pair into the dictionary
            dicts[value] = idx

            # iterate the whole process until the end of the string
        return maxlength



