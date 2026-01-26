class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        n,minimum_diff=len(arr),float('inf')
        for i in range(1,n):
            if arr[i]>arr[i-1]:
              minimum_diff=min(minimum_diff,arr[i]-arr[i-1])
        pairs=[]
        for i in range(1,n):
            if arr[i]>arr[i-1] and arr[i]-arr[i-1]==minimum_diff:
                pairs.append([arr[i-1],arr[i]])
        return pairs
    
     


class TestApp:
    def test_case_one(self):
        assert Solution().minimumAbsDifference([4,2,1,3])==[[1,2],[2,3],[3,4]]
    def test_case_two(self):
        assert Solution().minimumAbsDifference([1,3,6,10,15])==[[1,3]]
    def test_case_three(self):
        assert Solution().minimumAbsDifference([3,8,-10,23,19,-4,-14,27])==[[-14,-10],[19,23],[23,27]]