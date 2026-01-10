class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n,m=len(s1),len(s2)
        dp=[[0 for _ in range(m+1)] for _ in range(n+1)]
        total=0
        for i in range(n):
            total+=ord(s1[i])
        for i in range(m):
            total+=ord(s2[i])
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+ord(s1[i-1])
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        i,j=n,m 
        lcs=0 
        string=""
        while i>0 and j>0:
            if s1[i-1]==s2[j-1]:
                lcs+=2*ord(s1[i-1])
                string+=s1[i-1]
                i-=1
                j-=1
            elif dp[i-1][j]>dp[i][j-1]:
                i-=1
            else:
                j-=1
        return total-lcs
        
class TestApp:
    def test_case_one(self):
        assert Solution().minimumDeleteSum("sea","eat")==231
    def test_case_two(self):
        assert Solution().minimumDeleteSum("delete","leet")==403