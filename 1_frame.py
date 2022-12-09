'''
2022/12/04
1. 게임이 시작되면 0~11 + 조커까지 흑/백 블럭 각각 한 세트씩 생성되고
플레이어들이 4개씩 나눠 갖는다
2. 각자의 덱에 가지고 있는 블럭은 왼쪽에서부터 작은 수로 정렬됨
3. 흑/백 블럭 모두 가지고 있는 경우는 흑 블럭이 왼쪽으로 오게 정렬한다
(보여주기 방식은 나중에 변경. 일단 플에이어 2명 기준, 절대 기준으로만 짜봄..
=> 내꺼는 왼쪽에서 오른쪽로 점점커지고, 상대 것은 오른쪽에서 왼쪽으로 점점 커짐)
4. 조커는 아무 곳에나 배치할 수 있다
=>플레이어가 배치 할 수 있어야 함.
5. 턴을 돌아가면서 블럭더미에서 블럭을 하나 가져오고, [2]조건에 맞도록 정렬,
방금 뽑은 카드가 무엇인지 표시해야함.
6. 해당 플레이어 턴에서 상대가 가지고 있는 블럭 중 한가지의 숫자를 맞힌다.
 1)맞히면 상대 맞혀진 타일이 공개됨
 2)틀리면 내가 방금 가져온 타일이 공개됨
 3)타일 추리에 성공하면 한 턴 더 공격(맞히기) 가능함./ 맞히지 않고 턴을 종료해도 괜찮음.
7. 상대의 모든 패를 공개하면 승리. 

<고도화>
1. 새로운 콘솔창에서 띄우기
2. 새 랜덤 더미 만드는 for문 업데이트
3. 더미에 남은 카드 수 표시
4. 처음 더미에서 뽑아오는 카드를 랜덤하게 부여하지 않고, 색깔 보고 뽑아오기.
=> 컴퓨터는 두개 두개 뽑아오게 하든지.. 하나의 색깔만 너무 뽑아오지 않게 해주기.(밸런스패치)
5. 시점 신경쓰기

'''

from random import *
import os                # 콘솔화 클리어명령어를 사용하기 위해 임포트
import re
import time
import keyboard

init_card = 4

player = []
enemy = []
dummy =[]

for i in range(0, 13) :   # 0~12 까지의 값 생성, 12 : 조커 
    card = "{0:02d}B".format(i) # int i를 표시해주는데, 2자리까지 표시하고 빈자리는 0으로 표기
    dummy.append(card)
    card = "{0:02d}W".format(i) 
    dummy.append(card)

shuffle(dummy)
#print(dummy)

#----- 4개 블럭 씩 나눠주기 

for i in range(init_card) :
    enemy.append(dummy.pop())
    player.append(dummy.pop())

enemy.sort()
player.sort()
              #enemy 가 가지고 있는 블럭 수 확인 
for i in range(len(enemy)) :            #enemy 블럭 출력
    if i < init_card-1 :               #출력 시 마지막 블럭에만 콤마를 빼기 위해 개행 조건 변경
        if "W" in enemy[i] :        #i번째 블럭에서 W(하얀색) 임을 확인 했다면 하얀색의 랜덤블럭(W?) 으로 출력
            print("W?", end=", ")
        else :
            print("B?", end=", ")
    else  :
        if "W" in enemy[i] :
            print("W?")
        else :
            print("B?")

'''
1____if 조커를 내가 갖고 있다면
2____다른 카드를 정렬해서 보여주고
3____조커를 어디에 배치할 지 선택하게 함
4____조커의 위치 고정해야함

와일문으로 텍스트 계속 리프레시 해주면서 방향키 입력받기
os.system('cls')

'''

print(player)

for i in range(len(player)) :                   # player가 조커를 가지고 있는지 확인
    if player[i].startswith('12') : 
        print("조커를 가지고 계시군요..")
        print("조커를 어디에 배치할까요?")
        place_of_joker = input()
        whatkindofjoker = player[i]
        del player[i]
        player.insert(int(place_of_joker )-1, whatkindofjoker)
        print("조커를 {0}번째에 배치함".format(place_of_joker))
        print(player)
        break

'''턴을 돌아가면서 블럭더미에서 블럭을 하나 가져오고, [2]조건에 맞도록 정렬,
방금 뽑은 카드가 무엇인지 표시해야함.'''

input("확인하셨다면 아무키나 누르세요. 다음 턴으로 넘어갑니다.")

os.system('cls')
print("더미에서 새로운 블럭을 가져옵니다")


enemy.append(dummy.pop())
for i in range(len(enemy)) :           #enemy 블럭 출력
    if i < len(enemy)-1 :              #출력 시 마지막 블럭에만 콤마를 빼기 위해 개행 조건 변경
        if "W" in enemy[i] :           #i번째 블럭에서 W(하얀색) 임을 확인 했다면 하얀색의 랜덤블럭(W?) 으로 출력
            print("W?", end=", ")
        else :
            print("B?", end=", ")
    else  :
        if "W" in enemy[i] :
            print("W?")
        else :
            print("B?")


player.append(dummy.pop())
print(player)


#새로 가져온 블럭이 조커인지 확인해야함.
#기존에 조커를 가지고 있었는지 확인해서, 재정렬 이후에 다시 조커 배치해야함
#정렬까지 한 다음에, 기존 조커자리와 새 블럭의 자리가 인접해있다면 조커를 다시 배치하면 되지 않을지?


#카드 패를 튜플로 바꿔서 오픈된 카드와 그렇지 않은 카드를 구분할 것.





#i=0
#while True:
#        for count in range()
#        print("{0}".format(i))
#        os.system('cls')
#        i=input()
#        time.sleep(1)


#running = True # 게임이 진행 중인가? True 일 때 진행 중.
#while running :
#break

 