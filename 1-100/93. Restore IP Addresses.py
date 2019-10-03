'''
Given a string containing only digits, 
restore it by returning all possible valid IP address combinations.

Example:
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
'''

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.dfs(s, 0, '', ans)
        return ans
    
    def dfs(self, s, num_part, path, ans):
        if num_part == 4:
            if not s:
                ans.append(path[:-1])
        else:
            for i in range(1, 4):
                # no more than the length of s
                if i <= len(s):
                    # choose one digit
                    if i == 1:
                        self.dfs(s[i:], num_part+1, path+s[:i]+'.', ans)
                    # choose two digits, and the first one shouldn't be '0'
                    elif i == 2 and s[0] != '0':
                        self.dfs(s[i:], num_part+1, path+s[:i]+'.', ans)
                    # choose three digits
                    elif i == 3 and s[0] != '0' and int(s[:3]) < 256:
                        self.dfs(s[i:], num_part+1, path+s[:i]+'.', ans)
# Runtime: 32 ms, faster than 98.09% of Python3 online submissions for Restore IP Addresses.
# Memory Usage: 13.8 MB, less than 5.56% of Python3 online submissions for Restore IP Addresses.
