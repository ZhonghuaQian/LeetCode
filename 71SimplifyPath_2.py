class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        tree = path.split('/')
        tree = list(filter(lambda x: x != '' and x != '.', tree)) #去除//之间的空位和'.'
        sim_tree = []
        for node in tree:
            if node != '..':
                sim_tree.append(node) #非空路径写进sim_tree
            elif sim_tree != []:
                sim_tree.pop() #如果非空，退到上一级目录
        sim_path = '/' + '/'.join(sim_tree) #写成目录形式
        return sim_path
                
'''
写程序有两种方式：胡乱凑答案，这里写一点补补，那里写一点，结果思路混乱；有个很清晰的思路，代码结构清晰，容易理解。
如果写一段时间，思路已经混乱了，应该停下来休息一下，或者换个时间再写。
'''
answer = Solution()
print(answer.simplifyPath('/a/./b/../../c'))