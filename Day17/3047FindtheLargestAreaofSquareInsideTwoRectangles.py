class Solution:
    def largestSquareArea(self, bottomLeft: list[list[int]], topRight: list[list[int]]) -> int:
        maximum_area=0
        n=len(bottomLeft)
        def helper(index:int,x_left=None,x_right=None,y_bottom=None,y_top=None,count:int=0):
            nonlocal maximum_area 
            if index==n:
                if count>=2 and x_left is not None and y_top>y_bottom and x_right>x_left :
                    side=min(x_right-x_left,y_top-y_bottom)
                    maximum_area=max(maximum_area,side**2)
                return 
            helper(index+1,x_left,x_right,y_bottom,y_top,count)
            btx,bty=bottomLeft[index]
            tpx,tpy=topRight[index]
            if x_left is None:
                helper(index+1,btx,tpx,bty,tpy,count+1)
            else:
                helper(index+1,
                       max(x_left,btx),
                       min(x_right,tpx),
                       max(y_bottom,bty),
                       min(y_top,tpy),
                       count+1)
        helper(0)
        return maximum_area

from itertools import combinations
class Solution:
    def largestSquareArea(self, bottomLeft: list[list[int]], topRight: list[list[int]]) -> int:
        maximum_area=0
        for (bt_left_i,tp_right_i),(bt_left_j,tp_right_j) in combinations(zip(bottomLeft,topRight),2):
            width=min(tp_right_i[0],tp_right_j[0])-max(bt_left_i[0],bt_left_j[0])
            height=min(tp_right_i[1],tp_right_j[1])-max(bt_left_i[1],bt_left_j[1])
            side=min(width,height)
            maximum_area=max(maximum_area,side)
        return maximum_area**2
class TestApp:
    
    def test_case_one(self):
        assert Solution().largestSquareArea(bottomLeft = [[1,1],[2,2],[3,1]], topRight = [[3,3],[4,4],[6,6]])==1
    def test_case_two(self):
        assert Solution().largestSquareArea(bottomLeft = [[1,1],[1,3],[1,5]], topRight = [[5,5],[5,7],[5,9]])==4
    def test_case_three(self):
        assert Solution().largestSquareArea(bottomLeft = [[1,1],[2,2],[1,2]], topRight = [[3,3],[4,4],[3,4]])==1
    def test_case_four(self):
        assert Solution().largestSquareArea([[1,4],[1,1],[3,8]],[[6,9],[6,4],[8,10]])==1