# week01_4.py
# LeetCode 151. Reverse Words in a String
# 將 words 裡的 word 倒過來放
class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split() # 把空白,把字斷成很多字
        ans = []
        for i in range(len(a)-1, -1, -1): # 倒過來的迴圈
            ans.append(a[i]) # 把字塞入ans裡
        return ' '.join(ans) # 把空格隔開、接成很長的字串