class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: list[int], vBars: list[int]) -> int:
        hBars.sort()
        vBars.sort()
        hmax=vmax=hcur=vcur=1
        for i in range(1,len(hBars)):
            if hBars[i]==hBars[i-1]+1:
                hcur+=1
            else:
                hcur=1
            hmax=max(hmax,hcur)
        for i in range(1,len(vBars)):
            if vBars[i]==vBars[i-1]+1:
                vcur+=1
            else:
                vcur=1
            vmax=max(vmax,vcur)
        side=min(hmax,vmax)+1
        return side**2
       
class TestApp:
    def test_case_one(self):
        assert Solution().maximizeSquareHoleArea(2,1,[2,3],[2])==4
    def test_case_two(self):
        assert Solution().maximizeSquareHoleArea(1,1,[2],[2])==4
    def test_case_three(self):
        assert Solution().maximizeSquareHoleArea(2,3,[2,3],[2,4])==4