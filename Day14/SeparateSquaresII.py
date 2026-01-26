class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        max_y=total_area=0  
        min_y=float('inf')
        for x,y,length in squares:
            max_y=max(y+length,max_y)
            total_area+=length**2 
            min_y=min(min_y,y)
        def helper(threshold:int):
            area=0
            for x,y,length in squares:
                if y<threshold:
                    area+=length*min(threshold-y,length)
            return area>total_area//2
        low,high=min_y,max_y 
        ans=float('inf')
        while (high-low)>1e-5:
              mid=(low+high)//2 
              if helper(mid):
                  high=mid 
                  ans=min(mid,ans)
              else:
                  low=mid 
        return ans
        