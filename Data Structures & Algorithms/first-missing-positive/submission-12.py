class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if(nums[i] < 0 or nums[i]>n):
                nums[i] = 0
        for i in range(n):
            val = nums[i] % (n+1)
            if val>0:
                nums[val - 1] += (n+1)
        for i in range(n):
            if nums[i]<n+1:
                return i+1
        return n+1