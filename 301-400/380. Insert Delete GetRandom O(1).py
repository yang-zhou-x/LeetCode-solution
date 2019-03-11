class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums=[]
        self.posi={}  # {val:索引}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.posi:
            self.nums.append(val)
            self.posi[val]=len(self.nums)-1
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.posi:
            idx=self.posi[val]
            last=self.nums[-1]
            # 将val替换为last后，直接删去原位置的last
            self.nums[idx]=last
            self.posi[last]=idx
            # remove
            self.nums.pop()
            self.posi.pop(val)
            return True
        else:
            return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# Runtime: 96 ms, faster than 74.46% of Python3 online submissions for Insert Delete GetRandom O(1).
# Memory Usage: 16.4 MB, less than 5.30% of Python3 online submissions for Insert Delete GetRandom O(1).
