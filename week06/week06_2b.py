# week06-2b.py 學習計畫 Bit Manipulation 第2題
# LeetCode 136. Single Number
# 保證有一個數字落單，把它找出來
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 可以使用 Bit XOR 速解法,又快、又省空間
        # XOR 「碰1次,開」「再碰1次,關」
        ans = 0
        for num in nums: # 針對每次出現的數
            ans = ans ^ num # 進行 XOR 運算
        return ans