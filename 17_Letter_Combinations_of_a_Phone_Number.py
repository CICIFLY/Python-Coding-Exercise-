'''
17. Letter Combinations of a Phone Number (Medium)
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        digit_map = {'0': '0', '1':'1', '2':['a','b','c'], 
            '3':['d','e','f'], '4':['g','h','i'],
            '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'],
            '8':['t','u','v'], '9':['w','x','y','z']}

        if len(digits) == 0 :
            return []

        # here must have double quotes in the brackets
        result = [""]       
        for digit in digits:
            # each time a digit is done, clear the list
            tmp_list = []
            key_list = digit_map[digit] 
            for letter in key_list:
                # result is empty for first digit. 
                # when it goes to the second digit, first digit's chars have been  
                # stored in the result
                for char in result:
                    tmp_list.append(char + letter)
            result = tmp_list   
        return result

        