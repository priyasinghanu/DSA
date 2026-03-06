class Solution:
    def checkOnesSegment(self, s):

        zero_found = False

        for ch in s:

            if ch == '0':
                zero_found = True

            if zero_found and ch == '1':
                return False

        return True