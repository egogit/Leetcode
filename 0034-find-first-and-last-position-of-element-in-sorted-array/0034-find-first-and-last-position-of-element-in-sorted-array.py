class Solution:
    def binSearch(self, low, high):
        if low <= high:
            mid = low + (high - low) // 2
            if self.nums[mid] < self.target:
                self.binSearch(mid + 1, high)
            elif self.nums[mid] > self.target:
                self.binSearch(low, mid-1)
            else:
                if mid < self.min:
                    self.min = mid
                if mid > self.max:
                    self.max = mid
                if mid > 0 and self.nums[mid-1] == self.target:
                    self.binSearch(low, mid-1)
                if mid < len(self.nums)-1 and self.nums[mid+1] == self.target:
                    self.binSearch(mid+1, high)


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums);
        self.nums = nums;
        self.min = float("inf");
        self.max = float("-inf");
        self.target = target

        if n == 0:
            return [-1,-1];

        low, high = 0, n - 1;
        
        self.binSearch(low, high);
        return [self.min, self.max] if self.max >= 0 else [-1,-1]