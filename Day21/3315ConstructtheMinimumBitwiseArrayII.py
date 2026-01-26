class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        n=len(nums)
        ans=[0]*n
        def helper(threshold:int):
            binary_string=list(bin(threshold)[2::])
            for i in range(len(binary_string)):
                curr=binary_string[i]
                binary_string[i]="1" if curr=="0" else "0"
                number=int("".join(binary_string),2)
                if number|(number+1)==threshold:
                    return number 
                binary_string[i]=curr
            return -1
        for i in range(n):
            ans[i]=helper(nums[i]) if nums[i]%2 else -1 
        return ans
        
        
class TestApp:
    def test_case_one(self):
        assert Solution().minBitwiseArray([2,3,5,7])==[-1,1,4,3]
    def test_case_two(self):
        assert Solution().minBitwiseArray([11,13,31])==[9,12,15]

 