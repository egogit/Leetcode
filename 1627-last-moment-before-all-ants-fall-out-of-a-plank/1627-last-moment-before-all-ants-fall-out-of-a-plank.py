class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        r = min(right) if right else n+1
        l = max(left) if left else -1

        return n-r if n-r>l-0 else l-0;