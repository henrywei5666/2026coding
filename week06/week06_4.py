# week06-4.py 學習計畫 Array / String 最後1題
# LeetCode 605. Can Place Flowers
#在長長的花壇flowerbed裡,1已經種花、還沒種花。花要間隔放
#問:能不能再種n盆花
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool: 
        N = len(flowerbed) # 有幾個格子
        if N==1 and flowerbed==[0]: return True #特殊狀況
        if N > 1 and flowerbed [0]==0 and flowerbed[1]==0: # 最左邊,可以種花嗎?
            flowerbed[0] = 1 #可以,種在最左邊
            n -= 1 # 解決掉1盆了
        for i in range(1, N-1): # (中間的部分)每格逐一檢查
            if flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                flowerbed[i] = 1 # 多種一盆花
                n -= 1 # 解決掉1盆了
        if N > 1 and flowerbed [N-2]==0 and flowerbed [N-1]==0: # 最右邊,可以種花嗎?        
            flowerbed [N-1] = 1 #可以,種在最右邊
            n -= 1 # 解決掉1盆了
        return n <= 0 # 把目標要種的花,都種完了,完成任務,開心