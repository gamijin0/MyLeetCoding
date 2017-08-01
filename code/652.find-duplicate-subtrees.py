#coding: utf-8
#
# [652] Find Duplicate Subtrees
#
# https://leetcode.com/problems/find-duplicate-subtrees
#
# algorithms
# Medium (26.35%)
# Total Accepted:    1.6K
# Total Submissions: 6.2K
# Testcase Example:  '[2,1,1]'
#
# 
# Given a binary tree, return all duplicate subtrees. For each kind of
# duplicate subtrees, you only need to return the root node of any one of
# them. 
# 
# 
# Two trees are duplicate if they have the same structure with same node
# values.
# 
# 
# Example 1: 
# 
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   2   4
# ⁠      /
# ⁠     4
# 
# The following are two duplicate subtrees:
# 
# ⁠     2
# ⁠    /
# ⁠   4
# 
# and
# 
# ⁠   4
# 
# Therefore, you need to return above trees' root in the form of a list.
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):


    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        self.res = []
        if(root is None):
            return []

        self.data = dict()

        self.traversal(root)




        return self.res

    def traversal(self,root):
        ls,rs = '',''
        lh,rh = 0,0

        s = 'm'+str(root.val)

        if(root.left):
            ls,lh= self.traversal(root.left)
            s+='l'+ls
        if(root.right):
            rs,rh = self.traversal(root.right)
            s += 'r' + rs

        h = max(lh,rh)+1

        if(h not in self.data):
            self.data[h] = dict()
            self.data[h][s] = 1
        else:
            if(s not in self.data[h]):
                self.data[h][s] = 1
            else:
                if(self.data[h][s] ==1):
                    self.res.append(root)
                    print(s)
                self.data[h][s]+=1

        return s,h


# if(__name__=="__main__"):
#     a1 = TreeNode(1)
#     a2 = TreeNode(2)
#     a3 = TreeNode(3)
#     a4 = TreeNode(4)
#     a5 = TreeNode(2)
#     a6 = TreeNode(4)
#     a7 = TreeNode(4)
#
#     a1.left = a2
#     a1.right = a3
#
#     a2.left = a4
#
#     a3.left = a5
#     a3.right = a6
#
#     a5.left = a7
#
#     one = Solution()
#     one.findDuplicateSubtrees(a1)