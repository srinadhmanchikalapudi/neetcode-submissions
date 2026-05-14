class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i,elem in enumerate(nums):
            if target - nums[i] in nums[i+1:]:
                x = target - nums[i]
                return [i, (nums[i+1:].index(x)+i+1)]