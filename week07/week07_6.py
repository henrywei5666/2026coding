# week07_6.py 學習計畫 Queue 第2題
# LeetCode 649. Dota2 Senate
# 從左到右輪,輪到的人,可把「後面任一個敵對陣營」除掉
# 巡完一輪,繞道前面繼續,直到全部字母相同,問最後「哪個陣營」得勝
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(list(senate))

        banR, banD = 0, 0 # 目前被消滅的次數,都還是0
        R,D = senate.count('R'),senate.count('D')
        while queue: # 進行「互相Ban對方」的遊戲
            now = queue.popleft() # 左邊兔出個字母,它要消滅「敵對陣營」
            if now == 'R':
                if banR > 0: # 已經紀錄要消滅1個人
                    banR -= 1 # 用掉1個消滅的名額
                    R -= 1 # 馬上少掉1個人
                    continue # 你一出現,就已經被消滅了(換下一位)
                else: # 你沒有被消滅,太好了,你可以反過來消滅對方
                    banD += 1
                    queue.append(now) # 再到最右邊排隊
            else:
                if banD > 0:
                    banD -= 1
                    D -= 1
                    continue
                else:
                    banR += 1
                    queue.append(now)

            if R==0: return 'Dire' # 把 R 消滅光,'D'就得勝
            if D==0: return 'Radiant' # 把 D 消滅光,'R'就得勝