'''
고도화 : 선 정하기 / 타일,블럭,카드 용어 통일 / 예외처리 숫자만 입력, 범위 내 입력 등 / 

'''

from random import *
import os               # 콘솔창 클리어 명령어를 사용하기 위해 임포트 
import re
import time
import msvcrt
import keyboard


def print_enemy():                          # enemy 의 카드는 플레이어에게 공개되지 않아야 하므로 별도의 함수로 마스킹해서 출력함 
    for i in range(len(enemy)) :            # enemy 가 가지고 있는 블럭 수 확인 
        if i < len(enemy)-1 :                 # 출력 시 마지막 블럭에만 콤마를 빼기 위해 개행 조건 변경
            if "W" in enemy[i] :            # i번째 블럭에서 W(하얀색) 임을 확인 했다면 하얀색의 랜덤블럭(W?) 으로 출력
                print("W?", end=", ")
            else :
                print("B?", end=", ")
        else :
            if "W" in enemy[i] :
                print("W?")
            else :
                print("B?")


os.system('cls')

init_block = 4

player = []
enemy = []
dummy =[]

#----- 게임 시작, 1set 26개 더미 블럭 만들기 
for i in range(0, 13) :             # 0~12 까지의 값 생성, 12 : 조커 
    block = "{0:02d}B".format(i)    # int i를 표시해주는데, 2자리까지 표시하고 빈자리는 0으로 표기(정렬 조건을 위해 우선 둠)
    dummy.append(block)
    block = "{0:02d}W".format(i) 
    dummy.append(block)


shuffle(dummy)
#print(dummy)

#----- 4개 블럭 씩 나눠주기 
for i in range(init_block) :   
    enemy.append(dummy.pop())
    player.append(dummy.pop())

enemy.sort()
player.sort()
              
print_enemy()
print(player)

for i in range(len(player)) :               # player가 조커를 가지고 있는지 확인
    if player[i].startswith('12') :
        print("조커를 가지고 계시군요..")
        print("조커를 어디에 배치할까요?")
        place_of_joker = input()  
        whatkindofjoker = player[i]
        del player[i]
        player.insert(int(place_of_joker) - 1, whatkindofjoker)
        print("조커를 {0}번째에 배치함".format(place_of_joker))
        print(player)
        break


print("확인하셨다면 아무키나 누르세요. 다음 턴으로 넘어갑니다.")
while True:
    if msvcrt.kbhit():
        break


# os.system('cls')

print("더미에서 새로운 블럭을 가져옵니다")
print("어떤색 타일을 가져올까요? W/B")
w_or_b = input()

while True:
    if w_or_b == "W":
        if "W" in dummy[len(dummy)-1] :
            player.append(dummy.pop())
            os.system('cls')
            print("흰색 블럭을 가져왔습니다.")
            break
        else : 
            shuffle(dummy) 
    elif w_or_b == "B":
        if "B" in dummy[len(dummy)-1] :
            player.append(dummy.pop())
            os.system('cls')
            print("검은색 블럭을 가져왔습니다.")
            break
        else : 
            shuffle(dummy) 
    else :
        print("W 또는 B라고 입력하세요.")
        w_or_b = input()

last_card = player[len(player)-1]
player[len(player)-1] = last_card + "★"
player.sort()


enemy.append(dummy.pop())
print_enemy()
print(player)
 

selected_enemy_card = 0
running = True # 게임이 진행 중인가? True일 때 진행 중.
while running:
    print("공격할 차례! 상대방의 카드 중 추리할 카드를 선택하세요 (방향키로 이동, 스페이스바로 선택)")
    if keyboard.is_pressed('left') and selected_enemy_card > 0: 
        selected_enemy_card -= 1       
    elif keyboard.is_pressed('right') and selected_enemy_card < len(enemy) - 1: 
        selected_enemy_card += 1
    elif keyboard.is_pressed('space') :
        guess = input("이 카드에 적힌 숫자는?")
        # block_com = "{0:02d}".format(int(guess))
        tmp = enemy[selected_enemy_card]
        if "{0:02d}".format(int(guess)) == tmp[0:2] :  
            # tmp(현재선택한 카드의값)의 0,1번째 문자열 가져옴.
            print("정답이에요~ 이제 상대 카드 중 맞춘 카드는 오픈된 채로 둡니다.")
        else : 
            print("땡 입니다..")
    else :
        pass
    
    for i in range(selected_enemy_card):
        print("   ", end=" ")
    print("▼")  
        
    print_enemy()
    print(player)   
        
    time.sleep(0.1)
    os.system('cls')



print("확인하셨다면 아무키나 누르세요. 다음 턴으로 넘어갑니다.")
while True:
    if msvcrt.kbhit():
        break

 



#새로 가져온 블럭이 조커인지 확인해야함
#기존에 조커를 가지고 있었는지 확인해서, 재정렬 이후에 다시 조커 배치해야함
# 정렬까지 한다음에, 기존 조커자리와 새 블럭의 자리가 인접해있다면 조커를 다시 배치하면 되지 않을지? 


#카드 패를 튜플로 바꿔서 오픈된 카드와 그렇지 않은 카드를 구분할 것. 




# running = True
# while running :
# break