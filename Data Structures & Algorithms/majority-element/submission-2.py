class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Boyer-Moore Voting Algorithm (O(n) time, O(1) space
        candidate, count = None, 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate