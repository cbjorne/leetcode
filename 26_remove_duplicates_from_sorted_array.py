# Simple approach, tracking index of last "inserted" value, while iterating array. Keeping track of values seen
class Solution(object):
    def removeDuplicates(self, nums):
        num_map = {}
        k = 0
        for i in range(len(nums)):
            if nums[i] not in num_map:
                num_map[nums[i]] = i
                nums[k] = nums[i]
                k += 1
        
        return k

s = Solution()
print(s.removeDuplicates([1,1,2]))
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))