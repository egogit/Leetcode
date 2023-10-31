class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        nums = [pref[0]];
        prev = pref[0];
        
        for i in range(1, len(pref)):
            nums.append(prev ^ pref[i])
            prev = pref[i];
        return nums;