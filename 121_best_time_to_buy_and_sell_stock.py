# Intuitive solution: track min price, on each iteration compare current with max and store max O(n) time O(1) space
class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        buy_price = prices[0]

        for i in range(1, len(prices)):
            if buy_price > prices[i]:
                buy_price = prices[i]

            max_profit = max(max_profit, prices[i] - buy_price)
        
        return max_profit

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([7,6,4,3,1]))