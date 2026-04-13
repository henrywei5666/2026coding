# week06-2a.py 學習計畫 Bit Manipulation 第2題
# LeetCode 136. Single Number
# 保證有一個數字落單，把它找出來
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums) # 上週 Hash Map/Hash Table 教過
        for c in counter: # 每次取出1個數,看它出現幾次
            if counter[c]==1: return c