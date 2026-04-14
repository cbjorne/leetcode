# Greedy approach, tracking the furthest reachable, and the current jump end. Increasing jumps
# when the current jump end is reached. The apprach works as the furthest reachable can only be
# reached when the current iteration is completed.

def jump(nums):
    jumps = 0
    current_jump_end = 0
    farthest_reachable = 0

    for i in range(len(nums)-1):
        farthest_reachable = max(farthest_reachable, i+nums[i])

        if current_jump_end == i:
            current_jump_end = farthest_reachable
            jumps += 1

    return jumps

print(jump([2,3,1,1,4]))
print(jump([2,3,0,1,4]))
