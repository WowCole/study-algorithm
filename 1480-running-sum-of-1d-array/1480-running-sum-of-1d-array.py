class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a=[]
        b=0
        for i in range (len(nums)) :
            b=b+nums[i]
            a.append(b)
        return a