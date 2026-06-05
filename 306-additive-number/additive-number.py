class Solution(object):
    def isAdditiveNumber(self, num):
        n = len(num)

        def check(a, b, start):
            while start < n:
                s = str(a + b)

                if not num.startswith(s, start):
                    return False

                start += len(s)
                a, b = b, a + b

            return True

        for i in range(1, n):
            for j in range(i + 1, n):

                # Leading zero check
                if num[0] == '0' and i > 1:
                    break

                if num[i] == '0' and j - i > 1:
                    continue

                a = int(num[:i])
                b = int(num[i:j])

                if check(a, b, j):
                    return True

        return False