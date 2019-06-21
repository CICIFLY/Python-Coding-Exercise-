"""
10. Regular Expression Matching (Hard)

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".

Example 5:
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""
*************************************************************************************
Notes: 
The function prototype should be: bool isMatch(const char *s, const char *p)

# dynamic programming
Dynamic Programming is mainly an optimization over plain recursion. 
Wherever we see a recursive solution that has repeated calls for same inputs, we can optimize it using Dynamic Programming.

The idea is to simply store the results of subproblems, so that we do not have to re-compute them when needed late

This simple optimization reduces time complexities from exponential to polynomial.

*************************************************************************************
Example with Fibonacci numbers:

recursive solution: exponential 
def fib(n):
	if n <= 1:
		return n
	return fib(n-1) + fib(n-2)

******************************
dynamic programming soluion: linear
def fib(n):
	fib[0] = 0
	fib[1] = 1
	for i in range(n):
		fib[i] = fib[i-1] +fib[i-2]
	return fib[n]
*************************************************************************************
solution:

Class solution:
    # @return a boolean
	def ismatch(self, s, p):
		dp = [ [False for i in range(len(p)+1)] for j in range(len(s)+1) ]
		dp[0][0] = True
		for i in range(1,len(p)+1):
			if p[i-1] == '*':
				if i >= 2:
					dp[0][i] = dp[0][i-2]

		for i in range(1,len(s)+1):
			for j in range(1,len(p)+1):
				if p[j-1] == '.':
					dp[i][j] = dp[i-1][j-1]
				elif p[j-1] == '*':
					dp[i][j] = dp[i][j-1] or dp[i][j-2] or (  dp[i-1][j] and ( s[i-1] == p[j-2] or p[j-2]=='.' )  )
				else:
					dp[i][j] = dp[i-1][j-1] and s[i-1] == p[j-1]
		return dp[len(s)][len[p]]

https://www.cnblogs.com/zuoyuan/p/3781773.html
https://leetcode.com/problems/regular-expression-matching/discuss/5723/My-DP-approach-in-Python-with-comments-and-unittest


modified code:
class Solution(object):
    def isMatch(self, s, p):
        m, n = len(s) + 1, len(p) + 1
        matches = [[False] * n  for _ in range(m)]

        # Match empty string with empty pattern
        matches[0][0] = True

        # Match empty string with .*
        for i, element in enumerate(p[1:], 2):
            matches[0][i] = matches[0][i - 2] and element == '*'

        for i, ss in enumerate(s, 1):
            for j, pp in enumerate(p, 1):
                if pp != '*':
                    # The previous character has matched and the current one
                    # has to be matched. Two possible matches: the same or .
                    matches[i][j] = matches[i - 1][j - 1] and \
                                    (ss == pp or pp == '.')
                else:
                    # Horizontal look up [j - 2].
                    # Not use the character before *.
                    matches[i][j] |= matches[i][j - 2]

                    # Vertical look up [i - 1].
                    # Use at least one character before *.
                    #   p a b *
                    # s 1 0 0 0
                    # a 0 1 0 1
                    # b 0 0 1 1
                    # b 0 0 0 ?
                    if ss == p[j - 2] or p[j - 2] == '.':
                        matches[i][j] |= matches[i - 1][j]

        return matches[-1][-1]
