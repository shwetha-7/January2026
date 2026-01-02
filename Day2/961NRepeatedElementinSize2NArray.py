class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        map={}
        for num in nums:
            if num in map: return num 
            map[num]=1
            
        