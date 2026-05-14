class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in range(0, len(nums)):
            d[nums[i]] = d.get(nums[i], 0) + 1
        
        y = []
        for i in range(0, k):
            max_key = max(d, key=d.get)
            y.append(max_key)
            d.pop(max_key)
        return y
