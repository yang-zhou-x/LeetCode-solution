'''
Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
All inputs will be in lowercase.
The order of your output does not matter.
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=collections.defaultdict(list)
        for s in strs:
            ans[''.join(sorted(s))].append(s)
        return list(ans.values())
# Runtime: 104 ms, faster than 99.89% of Python3 online submissions for Group Anagrams.

# 20190724
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for s in strs:  # 字母组合作为key，含相同字母的字符串hash到一起
            res[''.join(sorted(s))].append(s)
        return list(res.values())
# Runtime: 112 ms, faster than 64.72% of Python3 online submissions for Group Anagrams.
# Memory Usage: 16.8 MB, less than 35.69% of Python3 online submissions for Group Anagrams.
