class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r
        
        while l <= r:
            m = (l + r) // 2
            total, ship = 0, 1
            for w in weights:
                if total + w > m:
                    total = 0
                    ship += 1
                total += w

            if ship <= days:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        
        return res