# Almost identical approach to 26 Remove Duplicates, with an additional check on the count of the value
# stored in the map.
class Solution(object):
    def removeDuplicates(self, nums):
        num_map = {}
        k = 0
        for i in range(len(nums)):
            if nums[i] not in num_map:
                num_map[nums[i]] = 1
                nums[k] = nums[i]
                k += 1
            elif nums[i] in num_map and num_map[nums[i]] < 2:
                num_map[nums[i]] += 1
                nums[k] = nums[i]
                k += 1
        
        return k

s = Solution()
print(s.removeDuplicates([1,1,1,2,2,3]))
print(s.removeDuplicates([0,0,1,1,1,1,2,3,3]))