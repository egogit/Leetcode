class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority = len(nums)//3;
        nums.sort();
        ans = list();

        cnt = 1;
        prev = nums[0];
        for i in range(1,len(nums)):
            if nums[i] == prev:
                cnt += 1;
            else:
                if cnt > majority:
                    ans.append(prev)
                prev = nums[i];
                cnt = 1;

        if cnt > majority:
            ans.append(nums[-1])
        
        return ans;