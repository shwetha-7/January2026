class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        n,m=len(matrix),len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j]=='0' or i==0:
                    matrix[i][j]=int(matrix[i][j])
                else:
                    matrix[i][j]=int(matrix[i-1][j])+int(matrix[i][j])
        def helper(arr:list[int]):
            max_area=0 
            stack=[]
            for i in range(m):
                while stack and arr[stack[-1]]>arr[i]:
                      value=arr[stack.pop()]
                      pse=stack[-1] if stack else -1 
                      max_area=max(max_area,value*(i-pse-1))
                stack.append(i)
            while stack:
                  value=arr[stack.pop()]
                  pse=stack[-1] if stack else -1 
                  max_area=max(max_area,value*(m-pse-1))
            return max_area
        max_area=0
        for i in range(n):
            max_area=max(max_area,helper(matrix[i]))
        return max_area 
class TestApp:
    def test_case_one(self):
        assert Solution().maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])==6 
    def test_case_two(self):
        assert Solution().maximalRectangle([["0"]])==0
    def test_case_three(self):
        assert Solution().maximalRectangle([["1"]])==1
        