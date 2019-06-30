'''
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        edit = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):  # edit[0][0]表示两字符串都为空的情况
            edit[i][0] = i
        for i in range(n + 1):
            edit[0][i] = i
        for i in range(1, m + 1):  # 经过edit[i][j]次变换后，
            for j in range(1, n + 1):  # word1[:i]==word2[:j]
                if word1[i-1] == word2[j-1]:
                    edit[i][j] = edit[i - 1][j - 1]
                else:
                    edit[i][j] = 1+min(edit[i - 1][j],  # word2插入1字符
                                       edit[i][j - 1],  # word2删除1字符
                                       edit[i - 1][j - 1])  # 替换1字符
        return edit[m][n]
