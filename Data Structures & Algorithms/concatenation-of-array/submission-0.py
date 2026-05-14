class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        d = len(nums)
        for i in range(0,(2*d)):
            if(i >= d):
                ans.append(nums[i-d])
                continue

            ans.append(nums[i])

        return ans

            
                