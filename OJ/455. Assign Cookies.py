# coding=utf-8
__author__ = 'arachis'
"""
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with; and each cookie j has a size sj.
If sj >= gi, we can assign the cookie j to the child i, and the child i will be content.
Your goal is to maximize the number of your content children and output the maximum number.
给孩子们分饼干，一个孩子最多一袋饼干；假设每一个孩子都对饼干袋里的饼干个数有期待数目，求出你最多能满足多少个孩子
Note:
You may assume the greed factor is always positive.
You cannot assign more than one cookie to one child.

Example 1:
Input: [1,2,3], [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.

Example 2:
Input: [1,2], [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2.
You have 3 cookies and their sizes are big enough to gratify all of the children,
You need to output 2.
"""
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g:孩子们的期待
        :type s: 饼干袋子
        :rtype: int
        两个数组升序排列，然后依次匹配，知道有一个数组到末尾
        """
        g = sorted(g)
        s = sorted(s)
        i , j = 0,0
        count = 0
        while( i< len(g) and j< len(s) ):
            if( s[j] >= g[i] ):
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        return count

# print Solution().findContentChildren(  [1,2,3], [1,1] )
# print Solution().findContentChildren(  [1,2], [1,2,3] )

