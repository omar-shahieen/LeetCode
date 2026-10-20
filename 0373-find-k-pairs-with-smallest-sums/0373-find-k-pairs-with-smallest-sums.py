class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    
        maxHeap = []

        for first in nums1:
            for second in nums2:
                total = first + second

                if len(maxHeap) == k and total >= -maxHeap[0][0]:
                    break

                if len(maxHeap) < k:
                    heapq.heappush(maxHeap, (-total, first, second))
                else:
                    heapq.heapreplace(maxHeap, (-total, first, second))

                    
        res = []

        while maxHeap:
            total ,first,second = heapq.heappop(maxHeap)
            res.append([first, second])

        return res[::-1]
