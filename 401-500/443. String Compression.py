'''
Given an array of characters, compress it in-place.
The length after compression must always be smaller than or equal to the original array.
Every element of the array should be a character (not int) of length 1.
After you are done modifying the input array in-place, return the new length of the array.
 
Follow up:
Could you solve it using only O(1) extra space?

Example 1:
Input:
["a","a","b","b","c","c","c"]
Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
 
Example 2:
Input:
["a"]
Output:
Return 1, and the first 1 characters of the input array should be: ["a"]
Explanation:
Nothing is replaced.
 
Example 3:
Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
 
Note:
All characters have an ASCII value in [35, 126].
1 <= len(chars) <= 1000.
'''

class Solution:
    def compress(self, chars: List[str]) -> int:
        cnt = 1
        left = 1  # 频数存放的位置
        for cha in chars[1:]:
            if cha == chars[left-1]:
                cnt += 1
            else:
                left = self.check_num(chars, left, cnt)
                chars[left] = cha
                cnt = 1
                left += 1
        # 最后一个频数
        if cnt == 1:
            pass
        else:
            left = self.check_num(chars, left, cnt)
        return left
    
    def check_num(self, chars, left, cnt):
        if cnt > 9:
            cnt = list(str(cnt))
            for c in cnt:
                chars[left] = c
                left += 1
        elif cnt > 1:
            chars[left] = str(cnt)
            left += 1
        return left  # 下一个character的位置
# Runtime: 64 ms, faster than 90.25% of Python3 online submissions for String Compression.
# Memory Usage: 14 MB, less than 6.25% of Python3 online submissions for String Compression.
