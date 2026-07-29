from random import Random
class RandomizedSet:
    """
    For insert and remove operations, a hash table immediately comes to mind
    since it provides O(1) average time for checking existence, adding, and deleting elements.
    However, hash tables don't support getting a random element efficiently - we'd need to
    iterate through all keys which takes O(n) time.

    For getRandom, an array is perfect because we can generate a random index and access
    that element in O(1) time. But arrays have a problem:
    removing an element from the middle takes O(n) time due to shifting elements.

    The key insight is to combine both data structures and use a clever trick for removal:
    ``The removal trick``: Instead of removing an element from the middle of the array (which would require shifting all subsequent elements),
    we swap the element to be removed with the last element in the array.
    Then we can simply pop the last element in O(1) time.
    We just need to update the hash table to reflect the new index of the swapped element.

    ``Swap and pop technique``.
    """

    def __init__(self):
        self.hash_table = dict()
        self.q = list()
        self.generator = Random()
        

    def insert(self, val: int) -> bool:
        
        if val in self.hash_table:
            return False
        
        self.q.append(val)
        index = len(self.q) - 1
        self.hash_table[val] = index
        return True

    def remove(self, val: int) -> bool:
        
        if val not in self.hash_table:
            return False
        
        index_to_remove = self.hash_table[val]
        last_element = self.q[-1]

        # Move the last element to the position of element to remove
        self.q[index_to_remove] = last_element
        self.hash_table[last_element] = index_to_remove

        # Remove the last element from list and the value from dictionary
        self.q.pop()
        del self.hash_table[val]

        return True

    def getRandom(self) -> int:

        index = self.generator.randint(0, len(self.q) - 1)
        return self.q[index]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


s = RandomizedSet()
p1 = s.insert(1)
print(f"{p1=}")
p2 = s.remove(2)
print(f"{p2=}")
p3 = s.insert(2)
print(f"{p3=}")
p4 = s.getRandom()
print(f"{p4=}")
p5 = s.remove(1)
print(f"{p5=}")
p6 = s.insert(2)
print(f"{p6=}")
p7 = s.getRandom()
print(f"{p7=}")