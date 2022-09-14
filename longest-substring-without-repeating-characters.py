class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mcount, count = 0, 0
        
        for x in range(len(s)):
            seen = []
            for y in range(x, len(s)):
                if y in seen: break
                seen += [y]
                count += 1
            
            if count > mcount: mcount = count
            count = 0
            
        return mcount