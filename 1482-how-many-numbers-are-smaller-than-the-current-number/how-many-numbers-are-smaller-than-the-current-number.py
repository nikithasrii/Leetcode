class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n=[]
        for i in nums:
            m=0
            for j in nums:
                if i>j:
                    m+= 1
            n.append(m)
        return n