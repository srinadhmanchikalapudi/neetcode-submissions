#Brute Force
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
       
        nums = [n for n in nums if n>0]

        if not nums:
            return 1

        nums.sort()

        dedup = []
        for n in nums:
            if not dedup or dedup[-1] !=n:
                dedup.append(n)
        if dedup[0] !=1:
            return 1
        for i in range(len(dedup)-1):
            if (dedup[i] + 1 != dedup[i+1]):
                return dedup[i]+1
        return dedup[-1]+1