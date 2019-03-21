class Solution:
    def partition(self, s: 'str') -> 'List[List[str]]':
        ans=[]
        self.dfs(s,[],ans)
        return ans
    
    def dfs(self,remain,path,ans):
        if not remain:
            ans.append(path) # path储存了所有回文片段
            return # 终止
        for i in range(1,len(remain)+1): # 切片，遍历
            if self.is_palindrome(remain[:i]):
                self.dfs(remain[i:],path+[remain[:i]],ans) # path记录当前的回文片段
    
    def is_palindrome(self,string): # 判断是否回文
        return string==string[::-1]
        
# Runtime: 96 ms, faster than 78.10% of Python3 online submissions for Palindrome Partitioning.
