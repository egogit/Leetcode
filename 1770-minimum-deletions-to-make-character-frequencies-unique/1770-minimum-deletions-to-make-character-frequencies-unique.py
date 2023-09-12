class Solution:
    def minDeletions(self, s: str) -> int:
        arr = [0]*26;
        ans = 0;

        for a in s:
            i = ord(a) - 97;
            arr[i] += 1;
        
        arr.sort(reverse=True);
        prev = arr[0];

        i = 1;
        while(i < 26 and arr[i] != 0):
            if 0 < prev <= arr[i]:
                ans += (arr[i]-prev+1)
                arr[i] = prev - 1;
            elif prev == 0:
                ans += arr[i];
                arr[i] = 0;

            prev = arr[i];
            i += 1;

        return ans;