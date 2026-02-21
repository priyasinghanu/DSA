class Solution(object):
    def makeLargestSpecial(self, s):
        
        if len(s) <= 2:
            return s
        
        count = 0
        start = 0
        result = []
        
        for i in range(len(s)):
            if s[i] == '1':
                count += 1
            else:
                count -= 1
            
            # When balanced
            if count == 0:
                # Recursively solve inside part
                inner = self.makeLargestSpecial(s[start+1:i])
                result.append("1" + inner + "0")
                start = i + 1
        
        # Sort in descending order
        result.sort(reverse=True)
        
        return "".join(result)