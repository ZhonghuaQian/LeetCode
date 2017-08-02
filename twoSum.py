# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 09:11:56 2017

@author: qzhoo
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    return i, j
                j += 1
        i += 1
        return "No answer!"

nums = [2, 7, 11, 15]
target = 18
answer = Solution()
i, j = answer.twoSum(nums, target)
print(i, j)