

```python
def mergeSort(nums): 
    if len(nums) >1: 
        mid = len(nums)//2  
        L = nums[:mid]  
        R = nums[mid:] 
  
        mergeSort(L)  
        mergeSort(R) 
  
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
  
 
def printList(nums): 
    for i in range(len(nums)):         
        print(nums[i],end=" ") 
    print() 
  
 
if __name__ == '__main__': 
    nums = [24, 11, 33, 5, 6, 19]  
    print ("Given array is", end="\n")  
    printList(nums) 
    mergeSort(nums) 
    print("Sorted array is: ", end="\n") 
    printList(nums) 
```

    Given array is
    24 11 33 5 6 19 
    Sorted array is: 
    5 6 11 19 24 33 
    


```python
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
```


```python
nums = [24, 11, 33, 5, 6, 19]
Solution().merge_sort(nums)
print (nums)
```

    [5, 6, 11, 19, 24, 33]
    
