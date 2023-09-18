class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        q = [];
        for row, group in enumerate(mat):
            power = 0;
            for i in group:
                if i==1:
                    power += 1;
                else:
                    break
            heapq.heappush(q, [power, row]);
        ans = [];

        for _ in range(k):
            _, idx = heapq.heappop(q);
            ans.append(idx);
        
        return ans;
        