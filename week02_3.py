# week02_3.py 學習計畫 Two Pointers 第2題
# LeetCode 392. Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        N1, N2 = len(s), len(t) #字串長度
        if N1 == 0: return True # 有陷阱: 如果左邊字串是空的,就不用比較
        i = 0 # i 從0開始
        for k in range(N2): # 右邊一個個去試
            if s[i] == t[k]: # 找到1個「左右」符合的
                i += 1 # 左邊 i 往右升一級
        if i==N1: # 左邊的 i 有走到左邊的結束
            return True  # 成功
        # 沒有走到最後,沒有比對成功
        return False # 失敗