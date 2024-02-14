class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive= []
        negative= []
        rearranged= []
        for i in nums:
            if i>=0:
                positive.append(i)
            else:
                negative.append(i)  
        for i in range(len(positive)):
            rearranged.append(positive[i])
            rearranged.append(negative[i])
        return rearranged