class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        heap = list();
        for i in range(len(dist)):
            heappush(heap, ceil(dist[i]/speed[i]));
        
        i = 0;
        ans = 0;
        while(heap):
            t = heappop(heap);
            if t - i > 0:
                ans += 1;
                i += 1;
            else:
                break;
        
        return ans;
