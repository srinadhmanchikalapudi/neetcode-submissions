class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums) / 2
        nums1 = set(nums)
        nums2 = list(nums1)
        for i in nums2:
            if nums.count(i) > l:
                return i