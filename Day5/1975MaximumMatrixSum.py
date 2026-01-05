class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        n=len(matrix)
        total=count=0
        max_value=float('inf')
        for i in range(n):
            for j in range(n):
                if matrix[i][j]<0:
                    count+=1
                matrix[i][j]=abs(matrix[i][j])
                max_value=min(max_value,matrix[i][j])
                total+=matrix[i][j]
        if count%2:
            total-=2*max_value 
        return total 
class TestApp:
      def test_case_one(self):
          assert Solution().maxMatrixSum([[1,-1],[-1,1]])==4
      def test_case_two(self):
          assert Solution().maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]])==16
      def test_case_three(self):
          assert Solution().maxMatrixSum([[2,9,3],[5,4,-4],[1,7,1]])==34
      def test_case_four(self):
          assert Solution().maxMatrixSum([[-1,0,-1],[-2,1,3],[3,2,2]])==15         
                
                
        
        
