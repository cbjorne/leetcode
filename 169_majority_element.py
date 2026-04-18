# Simple pythonic approach is to sort the array and return the value at (len(nums)//2)) + 1
# Additional unoptomized approach to store all values and occurrances in hash map, then iterate over 
# k,v to find maximal (works for non majority as well)

# Unintuitive approach Moore voting, store curr and votes, if element does not match curr decrease vote
# Otherwise increase vote, switch candidate to next occurrance. Majority element cannot be "voted out"
class Solution(object):
    def majorityElement(self, nums):
        curr = 0
        votes = 0

        for i in nums:
            if votes == 0:
                curr = i
                votes += 1
            elif i == curr:
                votes += 1
            elif i != curr:
                votes -= 1
        
        return curr

s = Solution()
print(s.majorityElement([3,2,3]))
print(s.majorityElement([2,2,1,1,1,2,2]))
print(s.majorityElement([3,3,4]))