class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        dict_ = Counter(hand)
        hand.sort()
        i = 0
        n = len(hand)
        while i < n:
            curr = hand[i]
            j = 0
            while j < W:
                if curr+j not in dict_:
                    return False
                dict_[curr+j] -= 1
                if dict_[curr+j] == 0:
                    del dict_[curr+j]
                j+=1
            while i < n and hand[i] not in dict_:
                i+=1
        return True
