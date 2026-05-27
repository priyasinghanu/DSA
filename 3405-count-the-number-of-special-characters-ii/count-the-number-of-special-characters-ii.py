class Solution(object):
    def numberOfSpecialChars(self, word):
        
        first_upper = {}
        last_lower = {}

        for i, ch in enumerate(word):

            if ch.islower():
                last_lower[ch] = i

            else:
                low = ch.lower()

                if low not in first_upper:
                    first_upper[low] = i

        count = 0

        for ch in last_lower:

            if ch in first_upper:

                if last_lower[ch] < first_upper[ch]:
                    count += 1

        return count