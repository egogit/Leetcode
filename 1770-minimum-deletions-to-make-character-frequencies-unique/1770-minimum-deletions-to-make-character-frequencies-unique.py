class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = Counter(s);
        ans = 0;
        freq = set();

        arr = sorted(cnt.values(), reverse=True);

        for fq in arr:
            if fq not in freq:
                freq.add(fq)
                continue;
            
            while fq > 0 and fq in freq:
                fq -= 1;
                ans += 1;
            
            freq.add(fq)

        return ans;