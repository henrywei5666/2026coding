# week06_3b.py 學習計畫 Bit Manipulation 第3題
# LeetCode 1318. Minimum Flips to Make a OR b Equal to c
# 你可在 a 和 b 動手腳,flip切換一些bits,希望 a OR b 得到 C
class Solution: # 目標「最少flip次數」
    def minFlips (self, a: int, b: int, c: int) -> int:
        # 善用 Bit 運算: AND OR NOT XOR
        # 0010
        # 0110
        # 先OR起來
        # 0110
        # 把 c「反過來」,所有的都變成1,再看a,b對應項有幾個1
        c2 = ~c # bitwise NOT 反過來
        ans = bin(a & c2).count('1') + bin(b & c2).count('1') # 需要「把0變成1」有幾個?
        ans += bin(c & ~(a | b)).count('1') # 需要「把1變成0」有幾個
        #合併的結果中,有1的項,都是有的,但若沒有,要補1
        return ans