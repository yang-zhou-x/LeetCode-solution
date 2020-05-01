'''
In a deck of cards, each card has an integer written on it.
Return true if and only if you can choose X >= 2 
such that it is possible to split the entire deck into 1 or more groups of cards, where:
Each group has exactly X cards.
All the cards in each group have the same integer.
 
Example 1:
Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].

Example 2:
Input: deck = [1,1,1,2,2,2,3,3]
Output: false´
Explanation: No possible partition.

Example 3:
Input: deck = [1]
Output: false
Explanation: No possible partition.

Example 4:
Input: deck = [1,1]
Output: true
Explanation: Possible partition [1,1].

Example 5:
Input: deck = [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2].
 
Constraints:
1 <= deck.length <= 10^4
0 <= deck[i] < 10^4
'''

from collections import Counter
from functools import reduce
from math import gcd

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        deck = Counter(deck)
        cnts = tuple(set(deck.values()))
        num = min(cnts)
        if num < 2:
            return False
        primes, x = [], 2
        while num > 1:
            if num % x == 0:
                primes.append(x)
                while num % x == 0:
                    num /= x
            x += 1
        for prime in primes:
            if all(list(map(lambda x: x % prime == 0, cnts))):
                return True
        return False
# Runtime: 148 ms, faster than 30.48% of Python3 online submissions for X of a Kind in a Deck of Cards.
# Memory Usage: 14 MB, less than 11.11% of Python3 online submissions for X of a Kind in a Deck of Cards.

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        cnts = tuple(set(Counter(deck).values()))
        return reduce(gcd, cnts) >= 2
# Runtime: 140 ms, faster than 71.78% of Python3 online submissions for X of a Kind in a Deck of Cards.
# Memory Usage: 14 MB, less than 11.11% of Python3 online submissions for X of a Kind in a Deck of Cards.
