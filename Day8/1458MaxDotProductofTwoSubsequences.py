class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        n,m=len(nums1),len(nums2)
        def helper(i:int,j:int):
            if i==n or j==m: return float('-inf')
            take=nums1[i]*nums2[j]+max(0,helper(i+1,j+1))
            skip_i=helper(i+1,j)
            skip_j=helper(i,j+1)
            return max(take,skip_i,skip_j)
        return helper(0,0)
class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        n,m=len(nums1),len(nums2)
        dp=[[-1 for _ in range(m)] for _ in range(n)]
        def helper(i:int,j:int):
            if i==n or j==m: return float('-inf')
            if dp[i][j]!=-1: return dp[i][j]
            take=nums1[i]*nums2[j]+max(0,helper(i+1,j+1))
            skip_i=helper(i+1,j)
            skip_j=helper(i,j+1)
            dp[i][j]=max(take,skip_i,skip_j)
            return dp[i][j]
        return helper(0,0)
        
class TestApp:
    def test_case_one(self):
        assert Solution().maxDotProduct([2,1,-2,5],[3,0,-6])==18
    def test_case_two(self):
        assert Solution().maxDotProduct([3,-2],[2,-6,7])==21
    def test_case_three(self):
        assert Solution().maxDotProduct([-1,-1],[1,1])==-1