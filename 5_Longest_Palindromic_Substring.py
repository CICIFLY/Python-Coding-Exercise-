#5. Longest Palindromic Substring (Medium)
#Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

#Example 1:
#Input: "babad"
#Output: "bab"
#Note: "aba" is also a valid answer.

#Example 2:
#Input: "cbbd"
#Output: "bb"

#Palindrome, Dynamic Programming and String Manipulation.
# analysis : two examples give us two forms of palindrom
# a letter as a center point(a) or a symmetric line (the one between two b(s) ) in the string.

class Solution:
	
	def getLongestPalindrome(self, s, l, r):
		"""
		this function will get the current longest palindrome
		type of s : string
		l,r: character
		"""

		# l >= 0 and r < len(s) these two condition to make sure it is within the string , not out of range
		# s[l] == s[r]: make sure left and right characters are the same
		# whenever one of the conditions can not be met, while loop stops 
		while l >= 0 and r < len(s) and s[l] == s[r]: 
			# when meeting the conditions, left and right both should be pushed to edges
			l -=1
			r +=1
		return s[l+1:r]

	
	def longestPalindrome(self, s:'str') -> 'str': 
		palindrome = ''

		# go through the whole string
		for i in range(len(s)):

			# case 1 : center point , starts from the same index
			len1 = len(self.getLongestPalindrome(s, i, i))
			# compare length and reassign value
			if len1 > len(palindrome):
				palindrome = self.getLongestPalindrome(s, i, i)


			# case 2: symmetric line
			len2 = len(self.getLongestPalindrome(s, i, i+1))
			# compare length and reassign value
			if len2 > len(palindrome):
				palindrome = self.getLongestPalindrome(s, i, i+1)

		return palindrome