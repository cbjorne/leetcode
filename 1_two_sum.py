# simple array hashing problem, iterates over the array storing any missing target values (nums[i] + x = target)
# in the dictionary. If the missing x value appears in the dictionary, return the index's
class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}

        for i in range(len(nums)):
            if nums[i] in num_map:
                return [i, num_map[nums[i]]]
            else:
                num_map[target - nums[i]] = i

s = Solution()
print(s.twoSum([2,7,11,15], 9))
print(s.twoSum([3,2,4], 6))
print(s.twoSum([3,3], 6))
