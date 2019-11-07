# MergeSort                                                      
 * 時間複雜度                                                   
 * Best Case：Ο(n log n)                                            
* Worst Case：Ο(n log n)
* Average Case：Ο(n log n)
* T(n) = MergeSort(左子數列) + MergeSort(右子數列) + Merge
     * = T(n/2) + T(n/2) + c×n = O(n log2n)
 * 空間複雜度(Space Complexity)：Ο(n)
* 需要暫時性的暫列存放每回合Merge後的結果
* 穩定性(Stable/Unstable)：穩定(Stable)
# HeapSort
* 時間複雜度(Time Complexity)
* Best Case：Ο(n log n)
* Worst Case：Ο(n log n)
* Average Case：Ο(n log n)
* 空間複雜度(Space Complexity)：Ο(1)
* 原地置換(In-Place)
* 穩定性(Stable/Unstable)：不穩定(Unstable)
