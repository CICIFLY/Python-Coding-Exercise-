"""
11. Container With Most Water (Medium)
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, 
which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.


Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""

# this question is to find the largest water area ( interval * height )
# moving left or right is depending on which one is bigger. Always move the smaller number coz we want to keep the larger number
# update result each time 

class Solution:
	def maxArea(self, height: List[int]) -> int:
		"""
		input: takes a list of integers 
		return : a int, which is the biggest area
		"""
		# initiate the left and right indices and the result
		left = 0
		right = len(height) - 1
		result = 0

		# make sure the left index is on the left side of right index
		while left < right : 
            
            # calculate the area
            # compare the height of left index and right index, choose smaller one
			water_area = (right - left) * min( height[left], height[right])  
            
			# update result
			if water_area > result:
				result = water_area
            
            # move the smaller one's index
			if height[left] > height[right]:
				right = right - 1
			else:
				left = left +1 

		return result 





