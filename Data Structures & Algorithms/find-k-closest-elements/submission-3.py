class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minheap = []
        res = []
        for a in arr:
            heapq.heappush(minheap, (abs(x - a), a))
        
        while k > 0:
            d, p = heapq.heappop(minheap)
            res.append(p)
            k -= 1
        
        res.sort()
        return res