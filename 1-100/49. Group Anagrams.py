class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=collections.defaultdict(list)
        for s in strs:
            ans[''.join(sorted(s))].append(s)
        return list(ans.values())
        
# Runtime: 104 ms, faster than 99.89% of Python3 online submissions for Group Anagrams.
