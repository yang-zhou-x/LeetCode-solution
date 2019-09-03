'''
Given two words (beginWord and endWord), and a dictionary's word list, 
find all shortest transformation sequence(s) from beginWord to endWord, such that:
Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:
Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

Example 1:
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

Example 2:
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''

from collections import defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]):
        if endWord not in wordList:
            return []
        wordList = set(wordList)
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]]
        while layer:  # BFS
            newlayer = defaultdict(list)
            for w in layer:  # layer[w]里的每个list以w结尾
                if w == endWord:  # 首次出现endWord时加入res，上一步时endWord被从词表
                    res = layer[w]  # 中删去，之后不会再加入res，
                    break  # 从而实现最短路径
                else:
                    for i in range(len(w)):
                        for cha in 'abcdefghijklmnopqrstuvwxyz':
                            neww = w[:i] + cha + w[i + 1:]
                            if neww in wordList:
                                newlayer[neww] += \
                                    [words + [neww] for words in layer[w]]
            wordList -= set(newlayer.keys())  # 要求找到最短的，所以可以直接减去
            layer = newlayer
        return res
# Runtime: 480 ms, faster than 54.33% of Python3 online submissions for Word Ladder II.
# Memory Usage: 16.8 MB, less than 16.67% of Python3 online submissions for Word Ladder II.


