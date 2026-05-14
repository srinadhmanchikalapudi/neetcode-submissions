class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        n = len(nums)
        diff = 0
        for i,n in enumerate(nums):
            diff = target - n
            if diff in map:
                return [map[diff], i]
            map[n] = i