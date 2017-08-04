# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 08:17:32 2017

@author: qzhoo
"""

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        tree = path.split('/')
        tree = list(filter(lambda x: x != '' and x != '.', tree)) #去除//之间的空位和'.'
        i = 0 #i表示当前节点及之前的节点数
        sim_tree = tree[:] #复制tree到sim_tree中
        for node in tree:
            if node == '..':
                sim_tree.pop(i)
                if i > 0:
                    sim_tree.pop(i - 1)
                    i -= 1
            else: 
                i += 1
                    
        sim_path = '/' + '/'.join(sim_tree)
        return sim_path

answer = Solution()
print(answer.simplifyPath('/a/./b/../../c'))