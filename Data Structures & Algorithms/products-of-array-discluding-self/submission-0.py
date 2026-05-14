class Solution:
    def multiplying(self, nums, idx):
        total = 1
        for i,v in enumerate(nums):
            if idx != i:
                total *= v
        return total

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        y = []

        for idx in range(len(nums)):
            y.append(self.multiplying(nums, idx))
        return y
        

    