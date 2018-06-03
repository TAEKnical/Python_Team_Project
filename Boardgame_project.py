#한명이 파산했을 때 2인비교 적용해야 함


import random
global rank

def game():
	choose_character()
	global User,AI1,AI2
	sutda(User,AI1,AI2)
	# player=User['이름']#캐릭터
	# player_money = User['Start_money']#돈
	# player_Skill_Percentage = User['Skill_Percentage'] #스킬성공화률
	# computer1 = AI1['이름']
	# computer1_money = AI1['Start_money']
	# computer1_skill_percentage = AI1['Skill_Percentage']
	# computer2 = AI2['이름']
	# computer2_money = AI2['Start_money']
	# computer2_skill_percentage = AI2['Skill_Percentage']

def fresh_deck():
	deck = []
	for i in range(10):
		deck.append(i+1)
		deck.append(-(i+1))
	random.shuffle(deck)
	return deck

def hit(deck):
    if deck == []:
        fresh_deck()
    return  (deck[0],deck[1:])

def show_cards(cards):
	for card in cards:
		print(card) # 패 표현방법 바꿔야됨

def more(message):
    answer = input(message)
    while not (answer == 'y' or answer == 'n'):
        answer = input(message)
    return answer == 'y'

#족보
def jokbo(cards,rank): #    !!!!!!!!!남호형파트 .수정필요!
#망통 rank-=1
	if 3 in cards and -7 in cards:
		rank -= 1
	elif -3 in cards and (7 in cards or -7 in cards):
		rank -= 1
	elif 2 in cards and (8 in cards or -8 in cards):
		rank -= 1
	elif -2 in cards and (8 in cards or -8 in cards):
		rank -= 1
#갑오 rank =1
	if abs(cards[0]) + abs(cards[1]) == 9 or abs(cards[0]) + abs(cards[1]) == 19:
		rank += 1
		if 1 in cards and 8 in cards:
			rank += 8
#세륙 rank =2
	if 4 in cards and (6 in cards or -6 in cards):
		rank += 2
	elif -4 in cards and (6 in cards or -6 in cards):
		rank += 2
#장사 rank=3
	if 4 in cards and (10 in cards or -10 in cards):
		rank += 3
	elif -4 in cards and (10 in cards or -10 in cards):
		rank += 3	
#장삥 rank=4
	if 1 in cards and (10 in cards or -10 in cards):
		rank += 4
	elif -1 in cards and (10 in cards or -10 in cards):
		rank += 4
#구삥 rank=5
	if 1 in cards and (9 in cards or -9 in cards):
		rank += 5
	elif -1 in cards and (9 in cards or -9 in cards):
		rank += 5
#독사 rank=6
	elif 1 in cards and (4 in cards or -4 in cards):
		rank += 6
	elif -1 in cards and (4 in cards or -4 in cards):
		rank += 6
#알리 rank=7
	if 1 in cards and (2 in cards or -2 in cards):
		rank += 7
	elif -1 in cards and (2 in cards or -2 in cards):
		rank += 7
#땡 rank=8
	if abs(cards[0]) == abs(cards[1]):
		rank += 8
#광떙 rank=9
	if 1 in cards and (3 in cards or 8 in cards):
		rank += 9
	elif 3 in cards and 8 in cards:
		rank += 10
	else:
		rank = 0
	return cards,rank
#끗 rank = 10
#떙잡이   
	if 3 in cards and 7 in cards:
		rank += 11
#사구
	if 4 in cards and (9 in cards or -9 in cards):
		rank += 12
	elif -4 in cards and (9 in cards or -9 in cards):
		rank += 12
#암행어사
	if 4 in cards and (7 in cards or -7 in cards):
		rank += 13
	elif -4 in cards and (7 in cards or -7 in cards):
		rank += 13

def jokbomoya(cards,rank):
	if rank == -1:
		print('망통')
	elif rank == 1:
		print('갑오')
	elif rank == 2:
		print('세륙')
	elif rank == 3:
		print('장사')
	elif rank == 4:
		print('장삥')
	elif rank == 5:
		print('구삥')
	elif rank == 6:
		print('독사')
	elif rank == 7:
		print('알리')
	elif rank == 8:
		print(abs(cards[0]),'땡')

	elif rank == 9:
		print('광땡')
	elif rank == 0:
		count = abs(cards[0])+abs(cards[1])
		if count >= 10:
			count -= 10
			print(count,'끗')
		else:
			print(count,'끗')
	elif rank == 11: #떙잡이
		print('땡잡이')
	elif rank == 12:
		print('사구')
	elif rank == 13:
		print('암행어사')

def player_menu():
	try:
		global name1, name2
		select='0'
		while True:
			print("=====================")
			print("1.베팅   2.체크   3.다이")
			print("4."+name1+"  5."+name2)
			print("=====================")
			select=input("선택 : ")
			if select=='1' or select=='2' or select=='3' or select=='4' or select=='5':
				break
		return select
	except KeyboardInterrupt:
		print("종료합니다.")
def player_betting(player_money,standard_pandon):
	player_betting_money=input("얼마를 베팅하시겠습니까? : ")
	if(int(player_betting_money) > player_money):
		print("가진 돈보다 많이 입력할 수 없습니다.")
		player_betting(player_money,standard_pandon)
	elif(int(player_betting_money) < 0):
		print("음수는 입력할 수 없습니다.")
		player_betting(player_money,standard_pandon)
	elif(int(player_betting_money) < standard_pandon):
		print("판돈보다 적게 입력할 수 없습니다.")
		player_betting(player_money,standard_pandon)
	else:
		return player_betting_money

def computer_betting(computer_money,standard_pandon,computer_rank):
	if computer_rank == -1:
		return 0
	elif computer_rank == 0:
		return standard_pandon
	elif computer_rank <= 3:
		return standard_pandon+10000000
	elif computer_rank <= 6:
		return standard_pandon+20000000
	else:
		return standard_pandon+30000000

def sutda(User,AI1,AI2):
	player_money = int(User['Start_money'])
	computer1_money = int(AI1['Start_money'])
	computer2_money = int(AI2['Start_money'])
	try:
		while(True):
			if player_money==0: #플레이어1 파산
				print("당신은 파산했습니다.")
				break
				#losecount+=1
				#try+=1
			if computer1_moeny==0:#컴퓨터1 파산
				pass
			if computer2_money==0:#컴퓨터2 파산
				pass
			if computer1_money==0 and computer2_money==0: #컴퓨터 둘다 파산
				print("승리하였습니다!")
				print("플레이어 자산 : ", player_money)
				#wincount+=1
				#try+=1
				break

			print("섯다 라운드 시작")
			deck = fresh_deck()
			computer1 = []
			computer2 = []
			player = []
			computer1_rank = 0
			computer2_rank = 0
			computer1_lowest=0
			compuetr2_lowest=0
			player_rank = 0
			betting_money = 0
			betting_stack = 0
			computer1_die=0
			computer2_die=0
			computer1_end=0
			computer2_end=0
			player_end=0
			computer1_betting_money=0
			computer2_betting_money=0
			standard_pandon = User['standard_pandon']


			print("기본베팅",standard_pandon,"씩 진행합니다.") #기본베팅
			player_money -= standard_pandon
			computer1_money -= standard_pandon
			computer2_money -= standard_pandon
			betting_money=3*standard_pandon
			print("총 판돈은",betting_money,"입니다.")


			card, deck = hit(deck)		#패돌리기
			player.append(card)
			card, deck = hit(deck)
			computer1.append(card)
			card, deck = hit(deck)
			computer2.append(card)
			card, deck = hit(deck)
			player.append(card)
			card, deck = hit(deck)
			computer1.append(card)
			card, deck = hit(deck)
			computer2.append(card)


			print("내 패는:")		#플레이어 패 보여주기
			count = 1
			for i in player:
				print(count,'번쨰 패 : ')
				if i == 1:
					print('1광입니다')
				elif i == 3:
					print('3광입니다')
				elif i == 8:
					print('8광입니다')
				else:
					print(abs(i),'월 끗입니다')
			count += 1


			player,player_rank = jokbo(player,player_rank)	#플레이어,컴퓨터 랭크 부여 및 보유금액 출력
			print("플레이어 보유금액 : ",player_money)
			print("com1 보유금액 :", computer1_money)
			print("com2 보유금액 :", computer2_money)
			jokbomoya(player,player_rank)
			computer1,computer1_rank = jokbo(computer1,computer1_rank)
			computer1_check_percentage = (computer1_rank*5) + 50 #족보에 따라 computer가 체크를 외칠 확률부여
			if computer1_rank == -1: #망통이면 체크를 절대 외치지 않도록
				computer1_check_percentage = 0
			computer2,computer2_rank = jokbo(computer2,computer2_rank)
			computer2_check_percentage = (computer2_rank*5) + 50 #족보에 따라 computer가 체크를 외칠 확률부여
			if computer2_rank == -1: #망통이면 체크를 절대 외치지 않도록
				computer1_check_percentage = 0
			player_check=False
			computer1_check=make_percentage(computer1_check_percentage) #make_percentage : 위에서 입력된 확률에 따라 T/F 부여
			computer2_check=make_percentage(computer2_check_percentage)


			computer1_lowest = computer1_rank*2000000 #컴퓨터가 자신의 족보에 따라 베팅하는 하한선
			computer2_lowest = computer2_rank*2000000
			

			select=player_menu() 	#라운드 진행시 플레이어 메뉴 출력
			if select == '1': #플레이어 베팅
				player_betting_money = int(player_betting(player_money,standard_pandon))
				player_money-=player_betting_money
				betting_money+=player_betting_money
				pre_person_stack=player_betting_money
				print("당신은",player_betting_money,"원을 베팅했습니다.")
				if computer1_check:#플레이어가 베팅하고, 컴퓨터1이 die하지 않을 경우(체크/베팅)
					computer1_die=False 
					if betting_money < computer1_lowest: #컴퓨터1 베팅
						computer1_betting_money = int(computer_betting(computer1_money,standard_pandon,computer_rank))
						betting_money+=computer1_betting_money
						computer1_money-=computer1_betting_money
						print("com1은",computer1_betting_money,"원을 베팅했습니다.")
						computer1_end=False
					else: #컴퓨터1 체크선언
						computer1_betting_money=pre_person_stack
						computer1_check=True
						betting_money+=computer1_betting_money
						computer1_money-=computer1_betting_money
						print("com1은",computer1_betting_money,"원을 베팅하고 체크를 선언했습니다.")
						computer1_end=True
				else: #컴퓨터1 다이
					print("com1은 다이를 선언했습니다.")
					computer1_end=True
					computer1_die=True
				if computer2_check: #플레이어가 베팅하고, 컴퓨터1이 선택하고, 컴퓨터2가 die하지 않을 경우(체크/베팅)
					computer2_die=False
					if betting_money < computer2_lowest: #플레이어가 베팅하고, 컴퓨터1이 선태갛고, 컴퓨터2가 베팅
						computer2_betting_money = int(computer_betting(computer2_money,standard_pandon,computer_rank))
						betting_money+=computer2_betting_money
						computer2_money-=computer2_betting_money
						print("com2는",computer2_betting_money,"원을 베팅했습니다.")
						computer2_end=False
					else:#컴퓨터2가 체크선언 
						computer2_betting_money=pre_person_stack
						computer2_check=True
						betting_money+=computer2_betting_money
						computer2_money-=computer2_betting_money
						print("com2는",computer2_betting_money,"원을 베팅하고 체크를 선언했습니다.")
						computer2_end=True
				else:#컴퓨터2 다이선언
					print("com2는 다이를 선언했습니다.")
					computer2_end-True
					computer2_die=True

				if(computer1_die==True and computer2_die==True): #컴1, 컴2가 다이했을 경우만 미리 출력
					print("플레이어가 승리했습니다.")
					player_money +=betting_money
					computer1_money -=computer1_betting_money
					computer2_money -=computer2_betting_money
					print("플레이어 보유금액 : ",player_money)
					print("com1 보유금액 :", computer1_money)
					print("com2 보유금액 :", computer2_money)
					continue




			elif select =='2': #플레이어메뉴->체크 선택으로 플레이어가 체크인 경우(3명 모두 체크를 원하면 패 오픈)
				print("당신은 체크를 선언했습니다.")
				player_check=True
				player_end = True
				if(computer1_end==True and computer2_end==True and player_end==True):
					if(computer1_die==True and computer2_die==False): #컴퓨터1이 다이, 플레이어와 컴퓨터2가 체크한경우
						print("패를 오픈합니다.")
						print("com1은 이미 다이를 선언했습니다.")
						computer1_rank = -2 #다이한 참가자의 랭크는 -2로 지정하여 winandlose함수에서 패자취급하도록
						WinandLose(player_rank,computer1_rank,computer2_rank)
					elif(computer1_die==False and computer2_die==True): #컴퓨터1이 베팅, 플레이어와 컴퓨터2가 체크한경우
						print("패를 오픈합니다.")
						print("com2는 이미 다이를 선언했습니다.")
						computer2_rank=-2	#다이한 참가자의 랭크는 -2로 지정하여 winandlose함수에서 패자취급하도록
						WinandLose(player_rank,computer1_rank,computer2_rank)
					elif(computer1_die==False and computer2_die==False): #컴퓨터1, 컴퓨터2 모두 다이하지 않고 세명모두 체크한경우
						print("패를 오픈합니다.")
						print("아무도 다이를 선언하지 않았습니다.")
						WinandLose(player_rank,computer1_rank,computer2_rank)



			elif select =='3': #플레이어메뉴->다이 선택으로 플레이어가 다이를 선언한 경우
				player_die = True
				player_end = True
				if computer1_die==True and computer2_die==True: #세명 모두 다이를 선언한 경우->리매치
					print("세 명 모두 다이를 선언했으므로 다시 진행합니다.")
					continue
				elif computer1_die==True and computer2_die==False:#2명 다이로 컴퓨터2의 승리
					player_rank=-2
					computer1_rank=-2
					WinandLose(player_rank,computer1_rank,computer2_rank)
				elif computer1_die==False and computer2_die==True:#2명 다이로 컴퓨터1 승리
					player_rank=-2
					computer2_rank=-2
					WinandLose(player_rank,computer1_rank,computer2_rank)

			elif select =='4':  #스킬1사용   !!!!정환이파트
				skill_1()
				# 베팅
				pass
			elif select =='5': #스킬2사용    !!!!정환이파트
				skill_2()
				# 베팅
				pass
	except KeyboardInterrupt:
		print("프로그램을 종료합니다.")


def WinandLose(player_rank,computer1_rank,computer2_rank):

	if player_rank == 11 and (computer1_rank == 8 or computer2_rank == 8):
		print('computer1의 족보는 : ')
		jokbomoya(computer1,computer1_rank)
		print('computer2의 족보는 : ')
		jokbomoya(computer2,computer2_rank)
		print("player가 땡잡이로 이겼습니다.")
		player_money += betting_money
		print('player money : ',player_money)
		print('computer1 money : ',computer1_money)
		print('computer2 money : ',computer2_money)

	elif computer1_rank == 11  and (computer2_rank == 8 or player_rank == 8):
		print('computer1의 족보는 : ')
		jokbomoya(computer1,computer1_rank)
		print('computer2의 족보는 : ')
		jokbomoya(computer2,computer2_rank)
		print("computer1이 땡잡이로 이겼습니다")
		computer1_money += betting_money
		print('player money : ',player_money)
		print('computer1 money : ',computer1_money)
		print('computer2 money : ',computer2_money)

	elif computer2_rank == 11  and (computer1_rank == 8 or player_rank == 8):
		print('computer1의 족보는 : ')
		jokbomoya(computer1,computer1_rank)
		print('computer2의 족보는 : ')
		jokbomoya(computer2,computer2_rank)
		print("computer2이 땡잡이로 이겼습니다")
		computer1_money += betting_money
		print('player money : ',player_money)
		print('computer1 money : ',computer1_money)
		print('computer2 money : ',computer2_money)

  #사구일 경우
	if  player_rank == 12 or computer1_rank == 12 or computer2_rank == 12:
     #자금
		print("49파토로 재경기합니다.")

  #암행어사일 경우
	if player_rank == 13 and (computer1_rank == 9 or computer2_rank == 9):
		print('computer1의 족보는 : ')
		jokbomoya(computer1,computer1_rank)
		print('computer2의 족보는 : ')
		jokbomoya(computer2,computer2_rank)
		print("player가 암행어사로 이겼습니다.")
		player_money += betting_money
		print('player money : ',player_money)
		print('computer1 money : ',computer1_money)
		print('computer2 money : ',computer2_money)

	elif computer1_rank == 13  and (computer2_rank == 9 or player_rank == 9):
		print('computer1의 족보는 : ')
		jokbomoya(computer1,computer1_rank)
		print('computer2의 족보는 : ')
		jokbomoya(computer2,computer2_rank)
		print("computer1이 암행어사로 이겼습니다")
		computer1_money += betting_money
		print('player money : ',player_money)
		print('computer1 money : ',computer1_money)
		print('computer2 money : ',computer2_money)
	elif computer2_rank == 13  and (computer1_rank == 9 or player_rank == 9):
		print('computer1의 족보는 : ')
		jokbomoya(computer1,computer1_rank)
		print('computer2의 족보는 : ')
		jokbomoya(computer2,computer2_rank)
		print("computer2이 암행어사로 이겼습니다")
		computer1_money += betting_money
		print('player money : ',player_money)
		print('computer1 money : ',computer1_money)
		print('computer2 money : ',computer2_money)
	if player_rank > computer1_rank and player_rank > computer2_rank:
		print('computer1의 족보는 : ')
		jokbomoya(computer1,computer1_rank)
		print('computer2의 족보는 : ')
		jokbomoya(computer2,computer2_rank)
		print("player win")
		player_money += betting_money
		print('player money : ',player_money)
		print('computer1 money : ',computer1_money)
		print('computer2 money : ',computer2_money)
	elif computer1_rank > computer2_rank and computer1_rank > player_rank:
		print('computer1의 족보는 : ')
		jokbomoya(computer1,computer1_rank)
		print('computer2의 족보는 : ')
		jokbomoya(computer2,computer2_rank)
		print("computer1 win")
		computer1_money += betting_money
		print('player money : ',player_money)
		print('computer1 money : ',computer1_money)
		print('computer2 money : ',computer2_money)
	elif computer2_rank > computer1_rank and computer2_rank > player_rank:
		print('computer1의 족보는 : ')
		jokbomoya(computer1,computer1_rank)
		print('computer2의 족보는 : ')
		jokbomoya(computer2,computer2_rank)
		print("computer2 win")
		computer2_money += betting_money
		print('player money : ',player_money)
		print('computer1 money : ',computer1_money)
		print('computer2 money : ',computer2_money)
	#rank가 같을경우 (끗/떙) 에서의 rank 비교
	elif player_rank == computer1_rank == computer2_rank:
		player_score = abs(player[0]) + abs(player[1])
		computer1_score = abs(computer1[0]) + abs(computer1[1])
		computer2_score = abs(computer2[0]) + abs(computer2[1])
		if player_score > computer1_score and player_score > computer2_score:
			print('computer1의 족보는 : ')
			jokbomoya(computer1,computer1_rank)
			print('computer2의 족보는 : ')
			jokbomoya(computer2,computer2_rank)
			print("player win")
			player_money += betting_money
			print('player money : ',player_money)
			print('computer1 money : ',computer1_money)
			print('computer2 money : ',computer2_money)
		elif computer1_score > computer2_rank and computer1_score > player_score:
			print('computer1의 족보는 : ')
			jokbomoya(computer1,computer1_rank)
			print('computer2의 족보는 : ')
			jokbomoya(computer2,computer2_rank)
			print("computer1 win")
			computer1_money += betting_money
			print('player money : ',player_money)
			print('computer1 money : ',computer1_money)
			print('computer2 money : ',computer2_money)
		elif computer2_score > computer1_score and computer2_score > player_score:
			print('computer1의 족보는 : ')
			jokbomoya(computer1,computer1_rank) 
			print('computer2의 족보는 : ')
			jokbomoya(computer2,computer2_rank)
			print("computer2 win")
			computer2_money += betting_money
			print('player money : ',player_money)
			print('computer1 money : ',computer1_money)
			print('computer2 money : ',computer2_money) # !!!! 남호형파트. 수정필요.


def choose_character():
	try:
	    character = input("캐릭터를 선택해 주세요. 1.정마담(하) 2.고광렬(중) 3.고니(상) ")
	    global User,AI1,AI2
	    while not (character == '1' or character == '2' or character == '3'):
	        character = input("캐릭터를 선택해 주세요. 1.정마담(하) 2.고광렬(중) 3.고니(상) ")
	    if character == '1':
	        User = {'이름' : '정마담' , 'Start_money' : 300000000, 'Skill_Percentage' : 80,'standard_pandon' : 10000000}
	        AI1 = {'이름' : 'Computer1', 'Start_money' : 200000000, 'Skill_Percentage' : 60, 'check_percentage' : 0}
	        AI2 = {'이름' : 'Computer2', 'Start_money' : 200000000, 'Skill_Percentage' : 60, 'check_percentage' : 0}
	    elif character == '2':
	        User = {'이름' : '고광렬' , 'Start_money' : 300000000, 'Skill_Percentage' : 70, 'standard_pandon' : 20000000}
	        AI1 = {'이름' : 'Computer1', 'Start_money' : 500000000, 'Skill_Percentage' : 70, 'check_percentage' : 0}
	        AI2 = {'이름' : 'Computer2', 'Start_money' : 500000000, 'Skill_Percentage' : 70, 'check_percentage' : 0}
	    elif character == '3':
	        User = {'이름' : '고니' , 'Start_money' : 300000000, 'Skill_Percentage' : 60, 'standard_pandon' : 30000000}
	        AI1 = {'이름' : 'Computer1', 'Start_money' : 1000000000, 'Skill_Percentage' : 80, 'check_percentage' : 0}
	        AI2 = {'이름' : 'Computer2', 'Start_money' : 1000000000, 'Skill_Percentage' : 80, 'check_percentage' : 0}
	    global ski1
	    ski1 = input("첫번째 스킬을 선택해주세요. 1.밑장빼기 2.바꿔치기 3.뻥카 4.훔쳐보기 ")
	    while not (ski1 == '1' or ski1 == '2' or ski1 == '3' or ski1 == '4'):
	        ski1 = input("1~4의 숫자로 선택해주세요. 1.밑장빼기 2.바꿔치기 3.뻥카 4.훔쳐보기 ")
	    global ski2
	    ski2 = input("두번째 스킬을 선택해주세요. ")
	    while not (ski2 == '1' or ski2 == '2' or ski2 == '3' or ski2 == '4') or ski2 == ski1:
	        if not (ski2 == '1' or ski2 == '2' or ski2 == '3' or ski2 == '4'):
	            ski2 = input("스킬목록에서 선택해주세요. 1.밑장빼기 2.바꿔치기 3.뻥카 4.훔쳐보기 ")
	        elif ski2 == ski1:
	            ski2 = input("이미 첫번째 스킬로 선택하셨습니다. 다른 스킬을 선택해주세요. ")
	    skill_confirm()
	except KeyboardInterrupt:
		print("종료합니다.")

def make_percentage(percent): #0~100숫자입력-> 확률
    skill_percentage = []
    for _ in range(100):
        skill_percentage.append(0)
    for _ in range(percent):
        skill_percentage.remove(skill_percentage[0])
        skill_percentage.append(1)
    random.shuffle(skill_percentage)
    if skill_percentage[0] == 1:
        return True #스킬 성공
    elif skill_percentage[0] == 0:
        return False #스킬 실패

def skill_confirm():
    global User , ski1 , ski2 , skill_1 , skill_2, name1, name2
    if ski1 == '1':
        name1='밑장빼기'
        def skill_1():
        	pass
    elif ski1 == '2':
        name1='바꿔치기'
        def skill_1():
        	pass
    elif ski1 == '3':
        name1='뻥카'
        def skill_1():
        	pass
    elif ski1 == '4':
        name1='훔쳐보기'
        def skill_1():
        	pass
    if ski2 == '1':
        name2='밑장빼기'
        def skill_2():
        	pass
    elif ski2 == '2':
        name2='바꿔치기'    	
        def skill_2():
        	pass
    elif ski2 == '3':
        name2='뻥카'
        def skill_2():
        	pass
    elif ski2 == '4':
        name2='훔쳐보기'
        def skill_2():
        	pass
def login(users):
	try:
		ID = input("ID를 입력하세요 : ")
		trypasswd = input("비밀번호를 입력하세요 : ")

		if ID in users: #로그인한 사용자 정보 초기화
			password = users[ID][0]
			tries = users[ID][1]
			wins = users[ID][2]
			money = users[ID][3]

			if trypasswd == password:
				print("로그인 되었습니다.")
			else:
				print("비밀번호가 틀립니다.")
				return login(users)
		else:
			users[ID] = (trypasswd, 0, 0, 0)
			return ID, 0, 0, 0, users
	except KeyboardInterrupt:
		print("종료합니다.")		

def load_users():
	file=open("users.txt", "r")
	users = {}
	for line in file:
		ID, password, tries, wins, money = line.strip('\n').split(',')
		users[ID] = (password,int(tries), int(wins), int(money))
	file.close()
	return users

def manual():
	try:
		while(True):
			print("----------게임설명----------")
			print("1.게임방식")
			print("2.스킬설명")
			print("3.난이도설명")
			print("4.대출시스템설명")
			print("5.이전 메뉴로")

			Select = input("Select : ")
			if Select=='1':
				print("게임방식")
			elif Select =='2':
				print("스킬")
			elif Select =='3':
				print("난이도")
			elif Select =='4':
				print("대출시스템")
			elif Select== '5':
				break
			else:
				print("올바르지 않은 입력입니다.")
	except KeyboardInterrupt:
		print("종료합니다.")

def main():
	try:
		while(True):
			print("-----------Welcome!-----------")
			print("-----------M e n u------------")
			print("1. 로그인 및 게임시작")
			print("2. 랭킹 보기")
			print("3. 게임설명(게임방식/스킬/난이도/대출시스템)")
			print("ctrl+c 를 입력하면 저장없이 프로그램을 즉시 종료합니다.")
			Select=input("Select : ")
			if Select=='1':
				users = load_users()
				login(users)
				game()
				break
			elif Select=='2':
				pass
			elif Select=='3':
				manual()
			else:
				print("올바르지 않은 입력입니다.")
	except KeyboardInterrupt:
		print("종료합니다.")
main()