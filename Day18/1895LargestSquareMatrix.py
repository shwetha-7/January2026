class Solution:
    def largestMagicSquare(self, grid: list[list[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        maximum_size,minimum_size=1,min(rows,cols)
        def helper(start_row:int,start_col:int,size:int)->bool:
            diagonal_left=diagonal_right=0
            for i in range(size):
                diagonal_left+=grid[start_row+i][start_col+i]
                diagonal_right+=grid[start_row+i][start_col+size-i-1]
            if diagonal_left!=diagonal_right: return False 
            # calculating rows 
            rows_sum=sum(grid[start_row][start_col:size+start_col:])
            if rows_sum!=diagonal_left: return False 
            for i in range(start_row+1,start_row+size):
                curr_sum=sum(grid[i][start_col:size+start_col:])
                if curr_sum!=rows_sum: return False 
            for j in range(start_col,start_col+size):
                curr_sum=0
                for i in range(start_row,start_row+size):
                    curr_sum+=grid[i][j]
                if curr_sum!=diagonal_left: 
                    return False 
            return True 
        
        for size in range(2,minimum_size+1):
            for row in range(rows-size+1):
                for col in range(cols-size+1):
                    if helper(row,col,size):
                        maximum_size=size 
        return maximum_size

class TestApp:
    def test_case_one(self):
        assert Solution().largestMagicSquare([[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]])==3
    def test_case_two(self):
        assert Solution().largestMagicSquare([[5,1,3,1],[9,3,3,1],[1,3,3,8]])==2