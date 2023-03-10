"""
세준이는 학교에서 집으로 가려고 한다. 
도시의 크기는 무한대이고, 도시의 세로 도로는 모든 정수 x좌표마다 있고, 가로 도로는 모든 정수 y좌표마다 있다. 
세준이는 현재 (0, 0)에 있다. 그리고 (X, Y)에 위치한 집으로 가려고 한다. 
세준이가 걸을 수 있는 방법은 두가지 인데, 
하나는 도로를 따라서 가로나 세로로 한 블록 움직여서 이번 사거리에서 저 사거리로 움직이는 방법이고,
또 하나는 블록을 대각선으로 가로지르는 방법이 있다.
세준이가 집으로 가는데 걸리는 최소시간을 구하는 프로그램을 작성하시오.

입력: 집의 위치 X Y, 걸어서 한 블록 가는데 걸리는 시간 W, 대각선으로 한 블록을 가로지르는 시간 S가 주어진다.
"""

x, y, w, s = list(map(int, input().split()))

#sol1: basic
sol1 = (x + y) * w

#sol2: 짝수 vs 홀수
if (x + y) % 2 == 0:
    sol2 = max(x, y) * s

elif (x + y) % 2 == 1:
    sol2 = (max(x, y) - 1) * s + w
    
#sol3: 대각선 + 평행 이동
sol3 = min(x, y)*s + (max(x, y)-min(x, y)) *w

print(min(sol1, sol2, sol3))

