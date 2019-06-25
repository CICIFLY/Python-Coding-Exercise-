'''
15. 3Sum (Medium)

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]



For time complexity
Sorting takes O(NlogN)
Now, we need to think if the 'nums' is really really big
We iterate through the 'nums' once, and each time we iterate the whole array again by a while loop
So it is O(NlogN+N^2)~=O(N^2)

For space complexity
We didnot use extra space except the 'res'
Since we may store the whole 'nums' in it
So it is O(N)
N is the length of 'nums'
'''
class Solution:

	def threeSum(self, nums):
		n = len(nums)
		result = []
		nums.sort()
		for i in range(n-2): 

			# if first element greater than 0 , no total would be 0
			if nums[i] > 0:
				break

			# i > 0 becuase when i = 0 , there is no previous element to compare with 
			# The continue command will skip the current round of for-loop, which removes the duplicate
			# This condition together can prevent duplication of data and TLE problem
			if i > 0 and nums[i] == nums[i-1]:
				continue

			l, r = i+1, n-1  
			while l < r :
				tmp = nums[i] + nums[l] + nums[r]
				# total less than 0, move right
				if tmp < 0:
					l += 1	
				# total greater than 0, move left 
				elif tmp > 0:
					r -= 1
				else:
					result.append([nums[i], nums[l], nums[r]])
					while l+1 < r and nums[l] == nums[l+1]:
						l += 1					
					while r-1 > l and nums[r] == nums[r-1]:
						r -= 1
					l += 1
					r -=1					
		return result 


