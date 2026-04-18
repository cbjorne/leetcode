# 2 pointer approach using existing m, and n values. The trick here is that if n > 0, the second array is empty and therefor the first
# array has all values sorted from array 2, and we can return. We do not need to check that both arrays have been sorted through
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        while n > 0:
            if m > 0 and nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        
        return nums1

s = Solution()
print(s.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
print(s.merge([1], 1, [], 0))
print(s.merge([0], 0, [1], 1))