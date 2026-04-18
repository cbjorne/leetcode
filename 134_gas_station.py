# greedy solution O(n) time O(1) space. Calculating total in loop prevents additional summation (minimal performance gain)
# Current gas is calculated at each step, if at any point it dips below zero, we know we cannot start from the previously
# > 0 solution
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        total = 0
        current_gas = 0
        start = 0

        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            current_gas += gas[i] - cost[i]

            if current_gas < 0:
                current_gas = 0
                start = i + 1
        
        if total < 0:
            return -1
        
        return start

s = Solution()
print(s.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
print(s.canCompleteCircuit([2,3,4], [3,4,3]))
print(s.canCompleteCircuit([5,8,2,8], [6,5,6,6]))

# Previous brute force over engineered solution. Similar implementation to above, but relies on multiple iterations
# over a diff array, which is not necessary. The key difference is the understanding that if the current index cannot
# complete the circuit, the circuit has to start one ahead (or not be completed at all)

# def canCompleteCircuit(gas, cost):
#     total = 0
#     diff = [0]*len(gas)

#     for i in range(len(gas)):
#         diff[i] = gas[i] - cost[i]
#         total += diff[i]

#     if total < 0:
#         return -1

#     max_idx = 0
#     max_diff = 0
#     curr_idx = -1
#     curr_diff = 0
#     n = len(diff)

#     for i in range(n*2):
#         curr_diff += diff[i%n]

#         if curr_diff >= 0 and curr_idx == -1:
#             curr_idx = i%n

#         if curr_diff > max_diff:
#             max_diff = curr_diff
#             max_idx = curr_idx
        
#         elif curr_diff < 0:
#             curr_diff = 0
#             curr_idx = -1
    
#     return max_idx
