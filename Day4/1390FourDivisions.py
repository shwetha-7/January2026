import math
class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        def helper(number:int):
            start,end=1,number**0.5 
            count=sum_total=0
            while start<=end:
                  if not number%start:
                      sum_total+=start
                      count+=1 
                      pos_div=number//start 
                      if pos_div!=start:
                          sum_total+=pos_div
                          count+=1 
                  start+=1
            return  count,sum_total     
        max_sum=0 
        for num in nums:
            res=helper(num)
            if res[0]==4:
                max_sum+=res[1]
        return max_sum 
    
class TestApp:
    def test_case_one(self):
        assert Solution().sumFourDivisors([21,4,7])==32
    def test_case_two(self):
        assert Solution().sumFourDivisors([21,21])==64
    def test_case_three(self):
        assert Solution().sumFourDivisors([1,2,3,4,5])==0