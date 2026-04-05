class Solution:
    def numberOfPairs(self, nums):
        pairs = 0
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for value in count.values():
            pairs += value // 2

        leftover = len(nums) - pairs * 2
        return [pairs, leftover]