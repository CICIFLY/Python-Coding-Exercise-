
# question: Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

python3 solution:
algorithm : has map 
Time complexity analysis
Traverse the array only once, O(n).

Space complexity analysis
Use hash table to store value and indices. For a list containing n values, the hash table will store at most n elements, O(n).

class solution(object):
	def twoSum(self, nums, target):
		'''
		type of nums: list[int]
		type of target: int
		return type: list[int]
		'''
		lookup = {}
		for idx, num in enumerate(nums):
			the_other_num = target - num
			if the_other_num in lookup:
				return [ lookup[the_other_num], idx]
			else:
				lookup[num] = idx


java solution
