# Greedy solution simply checks for previous day price, if less profit the difference.
# Simpler than local minima and maxima as multiple trades are allowed O(n) time O(1) space

def maxProfit(prices):
    profit = 0

    for i in range(1, len(prices)):
        if prices[i - 1] < prices[i]:
            profit += prices[i] - prices[i -1]
    
    return profit


print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([1,2,3,4,5]))
print(maxProfit([7,6,4,3,1]))