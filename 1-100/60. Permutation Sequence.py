'''
The set [1,2,3,...,n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:
Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.

Example 1:
Input: n = 3, k = 3
Output: "213"

Example 2:
Input: n = 4, k = 9
Output: "2314"
'''

from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        candidates = [x for x in range(1, n+1)]
        ans = []
        while k > 0:
            tmp = factorial(n-1)
            idx, remain = divmod(k, tmp)
            if idx:  # idx >= 1，即k > tmp
                if remain == 0:  
                    if n > 1: # 刚好是某组数的最后1个，如[1, 4,3,2]
                        ans.append(candidates[idx - 1])
                        candidates = candidates[:idx-1] + candidates[idx:]
                        ans += reversed(candidates)
                    else:  # candidates只剩1个时
                        ans += candidates
                    return ''.join(str(x) for x in ans)
                ans.append(candidates[idx])  # 下1位
                # 去掉第idx+1大的数字，即加入ans的数字
                candidates = candidates[:idx] + candidates[idx+1:]
                k = remain
            else:  # 跳过这1位
                ans.append(candidates[0])
                candidates = candidates[1:]
            n -= 1
# Runtime: 36 ms, faster than 79.38% of Python3 online submissions for Permutation Sequence.
# Memory Usage: 13.9 MB, less than 8.33% of Python3 online submissions for Permutation Sequence.
