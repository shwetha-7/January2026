class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry=0
        n=len(digits)
        digits[-1]+=1
        for i in range(n-1,-1,-1):
            sum=digits[i]+carry
            digits[i]=sum%10
            carry=sum//10 
            if not carry:
                break 
        if carry:
            return [carry]+digits 
        return digits
        
class TestApp:
    def test_case_one(self):
        assert Solution().plusOne([1,2,3])==[1,2,4]
    def test_case_two(self):
        assert Solution().plusOne([4,3,2,1])==[4,3,2,2]
    def test_case_three(self):
        assert Solution().plusOne([9])==[1,0]