class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        nums1 = list(nums)
        for i in nums1:
            if i == val:
                nums.remove(i)
            else:
                k = k + 1
        return k

