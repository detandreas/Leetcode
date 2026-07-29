from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """O(nlogn) it's really fast because of c implementation of sorted."""
        
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        ordered = sorted(freq.items(), key=lambda f: f[1], reverse=True)

        out = []
        for i in range(k):
            out.append(ordered[i][0])

        return out

import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """O(nlogk) using a min-priority queue."""
        
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        heap = []
        for num, freq in freq.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        out = []
        for freq, num in heap:
            out.append(num)

        return out


test = {"a": 1, "b": 2}
print(test.items())