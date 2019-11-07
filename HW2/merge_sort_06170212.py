class Solution(object):
    def merge_sort(self, nums):
        if len(nums) >1: 
            mid = len(nums)//2  
            L = nums[:mid]  
            R = nums[mid:] 
  
            self.merge_sort(L)  
            self.merge_sort(R) 
  
            i = j = k = 0       
        
            while i < len(L) and j < len(R): 
                if L[i] < R[j]: 
                    nums[k] = L[i] 
                    i+=1
                else: 
                    nums[k] = R[j] 
                    j+=1
                k+=1
                    
            while i < len(L): 
                nums[k] = L[i] 
                i+=1
                k+=1
          
            while j < len(R): 
                nums[k] = R[j] 
                j+=1
                k+=1
                nums = [24, 11, 33, 5, 6, 19]
Solution().merge_sort(nums)
print (nums)
[5, 6, 11, 19, 24, 33]
