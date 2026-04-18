# Python simplifies this problem by allowing in place pop of element. Simply track the length of nums and an iterator
class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums.pop(i)
                n -= 1
            else:
                i += 1
        
        return n

s = Solution()
print(s.removeElement([3,2,2,3], 3))
print(s.removeElement([0,1,2,2,3,0,4,2], 2))