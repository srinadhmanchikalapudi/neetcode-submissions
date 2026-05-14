class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        print(nums) #we get extra values at end after replacing the val in nums with next elems. but, no issues as we only consider first k elements.
        return k