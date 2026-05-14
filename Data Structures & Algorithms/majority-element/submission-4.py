class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        c = 0
        b = 0
        for n in nums:
            if n not in d.keys():
                d[n] = 1
            else:
                d[n]+=1
        print(d)
        for i,elem in d.items():
            
            print(i,elem)
            if elem >= c:
                c = elem
                b = i
            

        return b
        