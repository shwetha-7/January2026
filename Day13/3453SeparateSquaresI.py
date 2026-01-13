class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        max_y=total_area=0
        min_y=float('inf')
        for square in squares:
            length,y=square[2],square[1]
            total_area+=length**2 
            max_y=max(max_y,y+length)
            min_y=min(min_y,y)
        def findTheRemainingArea(threshold):
            area=0
            for x,y,length in squares:
                if y<threshold:
                    area+=length*min(threshold-y,length)
            return area>=total_area/2 
        low,high=min_y,max_y
        ans=float('inf')
        while (high-low)>1e-5:
              mid=(high+low)/2 
              if findTheRemainingArea(mid):
                  ans=min(mid,ans)
                  high=mid
              else:
                  low=mid
        return ans
class TestApp:
      def test_case_one(self):
          assert Solution().separateSquares([[0,0,1],[2,2,1]])==1.0000
      def test_case_two(self):
          assert Solution().separateSquares([[0,0,2],[1,1,1]])==1.16667
    