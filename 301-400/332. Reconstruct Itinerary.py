'''
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], 
reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. 
Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary 
that has the smallest lexical order when read as a single string. For example, 
the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.

Example 1:
Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Example 2:
Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
'''

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            targets[a].append(b)
        route, stack = [], ['JFK']
        while stack:
            while targets[stack[-1]]:
                stack.append(targets[stack[-1]].pop())
            route.append(stack.pop())
        return route[::-1]
# Runtime: 92 ms, faster than 70.79% of Python3 online submissions for Reconstruct Itinerary.
# Memory Usage: 14.1 MB, less than 6.67% of Python3 online submissions for Reconstruct Itinerary.
