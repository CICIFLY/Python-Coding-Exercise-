26. Questions: 
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
In-place means you can not create another list 
Solution:

class Solution:

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        i=0
        sorted(nums)
        while i < l-1:
            if nums[i] == nums[i+1]:
                del(nums[i])
                l -= 1
            else:      # here there must be “else”, can not just write the statement. Otherwise, only deleted the first repeated one 
                i += 1
        return len(nums)
        


27. Remove certain elements from an array 
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
Note that the order of those five elements can be arbitrary.


solution:

class Solution:
    def removeElement(self, nums, val):   
        l = len(nums)
        if l == 0:
            return 0
        i = 0
        while i < l:
            if nums[i] == val:
                nums.pop(i)
                l-=1
            else:
                i+=1
        return len(nums)
 
35.  Search insert position
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You may assume no duplicates in the array
二分查找每次能够排除掉一半的数据，查找的效率非常高，但是局限性比较大。 必须是有序序列才可以使用二分查找。      
My solution

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        start,end = 0,len(nums)-1
        if len(nums) == 0:  # remember to consider length is 0 case
            return start
       
        while start < end:
            mid = (start+end)//2   # index with index , number compares with number
            if target < nums[mid]:   # not compare target and nums[mid]
                end = mid-1
            elif target > nums[mid] :
                start = mid+1
            else:
                return mid
        # when start == end, only 1 element left, loop the following 
        if target <= nums[start]:
            return start
        else:
            return start+1

S = Solution()   # test cases
result1 = S.searchInsert([1,3,5,6], 5)
result2 = S.searchInsert([1,3,5,6], 2)
result3 = S.searchInsert([1,3,5,6], 7)
result4 = S.searchInsert([1,3,5,6], 0)
result5 = S.searchInsert([], 1)
result6 = S.searchInsert([1], 2)

print(result1, result2, result3, result4, result5, result6)
        
