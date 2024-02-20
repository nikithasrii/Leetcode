class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        total=(n+1)*n//2
        l_sum=sum(nums)
        m_num=total-l_sum
        return m_num