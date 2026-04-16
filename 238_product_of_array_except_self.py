# Unintuitive solution, prefix and suffix array, cumulutive sum is stored in prefix and suffix arrays, then multiplying
# them together provides answer array. Solution can be modeled by hand
# Input
# [1,2,3,4]
# Prefix
# [1, 1, 2, 6]
# Suffix
# [24, 12, 4, 1]
# Answer
# [24, 12, 8, 6]

def productExceptSelf(nums):
    n = len(nums)
    prefix = [1]*n
    suffix = [1]*n
    ans = [0]*n

    for i in range(1, n):
        prefix[i] = nums[i-1] * prefix[i-1]
    
    for j in range(n-2, -1, -1):
        suffix[j] = suffix[j+1] * nums[j+1]
    
    for k in range(n):
        ans[k] = prefix[k] * suffix[k]
    
    return ans



print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))