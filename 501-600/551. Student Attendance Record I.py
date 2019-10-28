'''
You are given a string representing an attendance record for a student. The record only contains 
the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) 
or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True

Example 2:
Input: "PPALLL"
Output: False
'''

class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') > 1:
            return False
        for i in range(1, len(s) - 1):
            if s[i-1] == s[i] == s[i+1] == 'L':
                return False
        return True
# Runtime: 36 ms, faster than 73.03% of Python3 online submissions for Student Attendance Record I.
# Memory Usage: 13.8 MB, less than 11.11% of Python3 online submissions for Student Attendance Record I.
