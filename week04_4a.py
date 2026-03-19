# week04_4a.py (重寫 week04_2.py)
# week04_2.py 學習計畫 prefix sum 第1題
# LeetCode 1732. Find the Highest Altitude
# 找到最高的海拔高度(一直加,就好了)
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = H = 0 # 一開始的高度是0
        for gg in gain: # Python 的進階 for 迴圈: 依序取出 gg
            H += gg
            ans = max(ans,H)
        return ans
