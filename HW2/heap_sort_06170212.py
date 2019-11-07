class Solution(object):
    def heap_sort(self, nums):              #第二個函數(for將Maxheap的結果排序成由小到大)
        n = len(nums)  
        for i in range(n, -1, -1): 
            self.heapify(nums, n, i) 
  
    
        for i in range(n-1, 0, -1):       #for i in range(n-1,0,-1): ==> for i in range(5,0,-1)arr[5]與 arr[0]值互換,因為經過前段程式arr[0]一定是此array的最大值而,arr[5}是最後一個陣列位置(arr[0],arr[1],arr[2],arr[3],arr[4],arr[5])因為互換後arr[0]已經不是最大值了,所以要再重作heapify
            nums[i], nums[0] = nums[0], nums[i]  
            self.heapify(nums, i, 0)
    def heapify(self,nums, n, i):    #第一個函數(for將原始Array排序成Maxheap的要求,就是Parent節點值一定比Children節點值大)
        largest = i       #此段是說明陣列的節點 l
        l = 2 * i + 1     #她的左子節點是2*1+1
        r = 2 * i + 2     #她的右子節點是2*1+2
 

        if l < n and nums[i] < nums[l]:   #看此次陣列的哪個做標值較大,將座標記錄下來
            largest = l 
  
    
        if r < n and nums[largest] < nums[r]:  #看此次陣列的哪個做標值較大,將座標記錄下來
            largest = r 
  
     
        if largest != i:        #判斷這次的Parent與Children作比較後,是否Children的值比Parent大,有的話做交換
            nums[i],nums[largest] = nums[largest],nums[i]  
  
        
            self.heapify(nums, n, largest)  #這邊是做遞迴它call自己Heapify為何要作遞迴,因為有作互換,要再以此重作一次Maxheap
            F=[24,11,33,5,6,19]
Solution().heap_sort(F)
print(F)
[5, 6, 11, 19, 24, 33]
