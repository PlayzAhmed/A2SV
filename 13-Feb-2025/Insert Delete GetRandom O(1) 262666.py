# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet(object):

    def __init__(self):
        self.mySet = []

    def insert(self, val):
        if val not in self.mySet:
            self.mySet.append(val)
            return True
        else:
            return False

        

    def remove(self, val):
        if val in self.mySet:
            self.mySet.remove(val)
            return True
        else:
            return False
        

    def getRandom(self):
        i = random.randint(0, len(self.mySet)-1)
        return self.mySet[i]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()