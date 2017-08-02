# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 13:05:01 2017

@author: qzhoo
"""
#用尾递归可以节省内存，永远不会有栈溢出问题，而且可以节省时间，调用函数是非常花时间的
class Solution(object):
    def climbStairs_tail(self, n, count1, count2):
        if n < 2:
            return count1
        return self.climbStairs_tail(n-1, count2, count1 + count2)
        
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.climbStairs_tail(n, 1, 2)
    

answer = Solution()
print(answer.climbStairs(2))