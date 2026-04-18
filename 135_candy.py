# Two pass solution checks all left and right neighbors and ensures ratings[i] > ratings[i+-1] have candies[i] > candies[i+-1]
# O(n) time O(n) space, specifically 3 passes of n. 
class Solution(object):
    def candy(self, ratings):
        ans = [1]*len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                ans[i] = ans[i-1]+1
        
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1] and ans[i] <= ans[i+1]:
                ans[i] = ans[i+1]+1
        
        return sum(ans)

s = Solution()
print(s.candy([1,0,2]))
print(s.candy([1,2,2]))
print(s.candy([1,2,3,4,5]))
print(s.candy([5,4,3,2,1]))
print(s.candy([1,3,2,2,1]))
print(s.candy([1,2,87,87,87,2,1]))