class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        for i in hand:
            start = i
            while count[start - 1]:
                start -= 1
            while count[start]:
                for j in range(start, start + groupSize):
                    if count[j] != 0:
                        count[j] -= 1
                    else:
                        return False
        return True

