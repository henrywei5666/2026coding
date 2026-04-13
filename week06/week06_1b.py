# week06-1b.py 學習計畫 Bit Manipulation 第1題
# LeetCode 338. Counting Bits
class Solution:
    def countBits (self, n: int) -> List[int]:
    #使用 Python 倒裝句,生成我們需要的陣列
        return [bin(i).count('1') for i in range(n+1)]