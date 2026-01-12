class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        count=0
        for i in range(1,len(points)):
            count+=max(abs(points[i-1][0]-points[i][0]),abs(points[i-1][1]-points[i][1]))
        return count
class TestApp:
    def test_case_one(self):
        assert Solution().minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])==7
    def test_case_two(self):
        assert Solution().minTimeToVisitAllPoints([[3,2],[-2,2]])==5