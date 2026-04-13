# week06-1a.py 學習計畫 Bit Manipulation 第1題
# LeetCode 338. Counting Bits
class Solution:
    def countBits (self, n: int) -> List[int]:
        ans = [] # 用來放我們的答案:0...n 的數,每個數「二進位表示」會有幾個1
        for i in range(n+1): #30...n
            # print(i, bin(i) ) # Debug 用的工具,了解「轉換二進位」的樣子
            # 字串.count('1') 會把字串裡面「有幾個字母 '1'數出來」
            ans.append( bin(i).count('1')) # 把數字塞入 ans 陣列的後面
        return ans