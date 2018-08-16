"""
Author: Vinh Truong

With given heights of blocks as [int], calculates
the amount of water trapped after raining. For
example, [0,2,0,1,2] would look like:

  [ ] X  X [ ]
__[ ]_X_[ ][ ]

where "[ ]" represents a block, and "X" represents
the water that is trapped.

trap(height) takes in an array of int, and returns
the n units of water trapped

This has O(n) time complexity
"""


def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    total = 0
    max = 0
    sub = 0
    for h in range(1,len(height)):
        sub += height[h]
        if height[h] >= height[max]:
            total += (height[max] * ((h-max)-1))
            total -= sub
            total += height[h]
            sub = 0
            max = h
    max2 = len(height)-1
    sub = 0
    for h in range(len(height)-2, max-1, -1):
        sub += height[h]
        if height[h] >= height[max2]:
            total += (height[max2] * ((max2-h)-1))
            total -= sub
            total += height[h]
            sub = 0
            max2 = h
    return total