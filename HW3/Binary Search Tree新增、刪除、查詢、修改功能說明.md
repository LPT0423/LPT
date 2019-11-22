# 新增
* 根據BST對Key之規則，先找到將要新增之node「適合的位置」
# 刪除
* 要在BST上執行刪除資料(被刪除的node稱為A)，必須讓刪除A後的BST仍然維持BST的性質。因此，所有「具有指向A的pointer」之node都必須調整該pointer，使其指向新的記憶體位置。
# 查詢
* BST的Search()操作，便是根據BST的特徵：Key(L)<Key(Current)<Key(R)，判斷Current應該往left subtree走，還是往right subtree走。
# 修改
* 給一個target後，把重複的節點換成另一個數值，改完後依照BTS的規則排序好。
