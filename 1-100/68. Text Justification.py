'''
Given an array of words and a width maxWidth, format the text such that each line has exactly 
maxWidth characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. 
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
Extra spaces between words should be distributed as evenly as possible. 
If the number of spaces on a line do not divide evenly between words, 
the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left justified and no extra space is inserted between words.

Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Example 1:
Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.

Example 3:
Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
'''

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        left = 0
        while left < len(words):
            used_len = 0
            used_words = []
            while left < len(words) \
                    and used_len + len(words[left]) <= maxWidth:
                used_words.append(words[left])
                used_len += len(words[left]) + 1  # 加上1个space
                left += 1
            if len(used_words) == 1:
                ans.append(used_words[0] + ' ' * (maxWidth - used_len + 1))
            elif used_len - 1 == maxWidth:  # 最后多了一个space，减去
                ans.append(' '.join(used_words))
            else:  # 没有刚好占用完的情况
                extra_len = maxWidth - used_len + 1
                intervals = len(used_words) - 1
                m, n = divmod(extra_len, intervals)  # 确定空格分布
                spaces = [' ' * (m + 1) for _ in range(intervals)]
                for i in range(n):
                    spaces[i] += ' '
                idx, res = 0, ''
                while idx < intervals:  # 合并
                    res += used_words[idx] + spaces[idx]
                    idx += 1
                res += used_words[idx]
                ans.append(res)
        last = [x for x in ans[-1].split() if x]  # 调整最后1个
        last = ' '.join(last)
        last += ' ' * (maxWidth - len(last))
        ans[-1] = last
        return ans
# Runtime: 36 ms, faster than 81.19% of Python3 online submissions for Text Justification.
# Memory Usage: 13.9 MB, less than 6.03% of Python3 online submissions for Text Justification.
