'''
We have two special characters. The first character can be represented by one bit 0. 
The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. 
Return whether the last character must be a one-bit character or not. 
The given string will always end with a zero.

Example 1:
Input: 
bits = [1, 0, 0]
Output: True
Explanation: 
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.

Example 2:
Input: 
bits = [1, 1, 1, 0]
Output: False
Explanation: 
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.

Note:
1 <= len(bits) <= 1000.
bits[i] is always 0 or 1.
'''

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 1:
            return True
        left = 0
        right = len(bits) - 1
        while left < right:
            if bits[left] == 0:
                left += 1
            else:
                left += 2
        # consider the last 3 digits
        if left == len(bits):
            return False
        return True
# Runtime: 48 ms, faster than 82.85% of Python3 online submissions for 1-bit and 2-bit Characters.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for 1-bit and 2-bit Characters.
