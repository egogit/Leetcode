from collections import defaultdict

class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = defaultdict(int);
        ans = 0;

        for a in s:
            cnt[a] += 1;

        arr = list();

        for a in cnt.values():
            arr.append(a);
        
        arr.sort(reverse=True)

        prev = arr[0];

        i = 1;
        while(i < len(arr)):
            if prev == 0:
                ans += sum(arr[i:]);
                break
            elif 0 < prev <= arr[i]:
                ans += (arr[i]-prev+1)
                arr[i] = prev - 1;

            prev = arr[i];
            i += 1;

        return ans;