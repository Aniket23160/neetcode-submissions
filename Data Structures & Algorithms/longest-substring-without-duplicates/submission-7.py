class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # d=[]
        if len(s)==1:
            return 1
        ans=0
        s=s+"$"
        for i in range(len(s)):
            d=[]
            for j in range(i,len(s)):
                # print(d)
                ans=max(ans,j-i)
                if s[j] not in d and s[j]!="$":
                    d.append(s[j])
                else:
                    break
        return ans


        