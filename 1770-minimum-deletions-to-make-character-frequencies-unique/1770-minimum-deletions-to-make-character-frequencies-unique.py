class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = Counter(s);
        ans = 0;
        freq = set();

        heap = list(cnt.values());
        heapq.heapify(heap);

        while heap:
            fq = heapq.heappop(heap)
            while fq > 0 and fq in freq:
                fq -= 1;
                ans += 1;
            freq.add(fq);

        return ans;