# Moving goal solution. Initialize a value at the last index. Iterate backwards through the array, at each step with a
# number greater than the current goal, set the goal to that index.
class Solution(object):
    def canJump(self, nums):
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= goal:
                goal = i

        return goal == 0

s = Solution()
print(s.canJump([2,3,1,1,4]))
print(s.canJump([3,2,1,0,4]))

