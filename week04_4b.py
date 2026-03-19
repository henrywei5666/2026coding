# week04_4b.py (重寫 week04_3.py)
# week04_3.py More Challenges 的簡單題
# LeeCode 3866. First Unique Even Element
# 找到陣列 nums 裡「只出現過1次的偶數」是誰
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        H = [0] * 200
        for nn in nums: # 把陣列的值, 逐一取出來
            H[nn] += 1 # 統計數量
        for nn in nums: # 再來一次, 逐一取出來
            if nn % 2 == 0 and H[nn] == 1: # 偶數 and 落單
                return nn
        return -1
       