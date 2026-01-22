class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        operations=0        
        def checkSortedOrNot(nums:list[int]):
            n=len(nums)
            for i in range(1,n):
                if nums[i-1]>nums[i]: return False 
            return True 
        
        while True:
            if checkSortedOrNot(nums): return operations 
            index,sum_total=-1,float('inf')
            for i in range(1,len(nums)):
                if (nums[i-1]+nums[i])<sum_total:
                    sum_total=nums[i-1]+nums[i]
                    index=i 
            operations+=1
            nums.pop(index)
            nums.pop(index-1)
            nums.insert(index-1,sum_total)

class TestApp:
    def test_case_one(self):
        assert Solution().minimumPairRemoval([5,2,3,1])==2
    def test_case_two(self):
        assert Solution().minimumPairRemoval([1,2,2])==0