class Solution:
    def maxSideLength(self, mat: list[list[int]], threshold: int) -> int:
        maximum_size=0 
        def helper(start_row:int,start_col:int,size):
            curr_sum=0
            for i in range(start_row,start_row+size):
                curr_sum+=sum(mat[i][start_col:start_col+size:])
            return curr_sum 
        rows,cols=len(mat),len(mat[0])
        minimum_size=min(rows,cols)
        for size in range(1,minimum_size):
            for row in range(rows-size+1):
                for col in range(cols-size+1):
                    res=helper(row,col,size)
                    if res<=threshold:
                        maximum_size=size 
        return maximum_size 

class TestApp:
    def test_case_one(self):
        assert Solution().maxSideLength([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]],4)==2
    def test_case_two(self):
        assert Solution().maxSideLength([[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]],1)==0           