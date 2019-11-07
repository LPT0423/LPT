# MergeSort
 * 時間複雜度
 * Best Case：Ο(n log n)
* Worst Case：Ο(n log n)
* Average Case：Ο(n log n)
* T(n) = MergeSort(左子數列) + MergeSort(右子數列) + Merge
     * = T(n/2) + T(n/2) + c×n = O(n log2n)
