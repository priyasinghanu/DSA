class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        xor_all = n
        
        for i in range(n):
            xor_all ^= i ^ nums[i]
            
        return xor_all