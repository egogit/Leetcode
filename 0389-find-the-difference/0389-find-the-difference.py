class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sc = Counter(s);
        ans = '';

        for letter in t:
            if letter in sc.keys():
                sc[letter] -= 1;
                if sc[letter] < 0:
                    ans = letter;
                    break;
            else:
                ans = letter;
                break;

        return ans;
        