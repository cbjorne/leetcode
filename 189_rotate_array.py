# Brute force solution: step through shifting each element for each k O(n * k) time O(1) space
# Intuitive solution, pointer for k, looping over elements and creating a new array O(n) time O(n) space 
# (does not work for in place rotation)
# Unintuitive approach: Optimized reversal, reverse the array, reverse 0:k, reverse n-k O(n) time (2 iterations of n) O(1) space

# Intuitive approach
# def rotate(nums, k):
#     ans = [0]*len(nums)
#     k = k % len(nums)

#     for i in range(len(nums)):
#         if k >= len(nums):
#             k = 0
#         ans[k] = nums[i]
#         k += 1

#     return ans

# Optimized Reversal
class Solution(object):
    def rotate(self, nums, k):
        k %= len(nums)

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, len(nums)-1)
        reverse(0, k-1)
        reverse(k, len(nums)-1)

        return nums

s = Solution()
print(s.rotate([1,2,3,4,5,6,7], 3))
print(s.rotate([-1,-100,3,99], 2))