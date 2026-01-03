class Solution:
    def numOfWays(self, n: int) -> int:
        mod=10**9+7
        a,b=[0]*n,[0]*n 
        a[0],b[0]=6,6
        for i in range(1,n):
            a[i]=(2*a[i-1]+2*b[i-1])%mod 
            b[i]=(2*a[i-1]+3*b[i-1])%mod
        return (a[n-1]+b[n-1])%mod 
    
class TestApp:
    def test_case_one(self):
        assert Solution().numOfWays(1)==12
    def test_case_two(self):
        assert Solution().numOfWays(5000)==30228214