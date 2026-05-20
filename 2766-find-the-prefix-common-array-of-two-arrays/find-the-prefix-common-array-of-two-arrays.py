class Solution(object):
    def findThePrefixCommonArray(self, A, B):

        seen = set()
        ans = []
        count = 0

        for i in range(len(A)):

            if A[i] in seen:
                count += 1
            else:
                seen.add(A[i])

            if B[i] in seen:
                count += 1
            else:
                seen.add(B[i])

            ans.append(count)

        return ans