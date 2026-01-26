import heapq
class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        operatiions=0
        def checkSortedOrNot(array:list[int]):
            n=len(array)
            for i in range(1,n):
                if array[i-1]>array[i]: return False 
            return True 
        hash_map={}
        for i in range(len(nums)):
            hash_map[i]=nums[i]
        while True: 
              if checkSortedOrNot(list(hash_map.values())): return operatiions
              queue=[]
              arr=list(hash_map.items())
              for i in range(1,len(arr)):
                  heapq.heappush(queue,[arr[i-1][1]+arr[i][1],arr[i-1][0],arr[i][0]])
              remove:list=heapq.heappop(queue)
              operatiions+=1
              del hash_map[remove[-1]]
              hash_map[remove[-2]]=remove[0]
              
class TestApp:
      def test_case_one(self):
          assert Solution().minimumPairRemoval([5,2,3,1])==2
      def test_case_two(self):
          assert Solution().minimumPairRemoval([1,2,2])==0