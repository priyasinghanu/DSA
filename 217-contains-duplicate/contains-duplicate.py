class Solution(object):
    def containsDuplicate(self, nums):
        if nums is None:
            return False

        if len(nums) != len(set(nums)):
            return True

        return False
       