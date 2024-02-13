class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        nsum=sum(nums)
        msum= 0
        for i in nums:
            for j in str(i):
                msum += int(j)
        return abs(nsum-msum)