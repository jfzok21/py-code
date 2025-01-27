import random
rd = input("ready? (y/n) ")
if rd == "y":
    player = random.randint(1,6)
    computer = random.randint(1,6)
    
    if player > computer:
        print(f'player:{player} \ncomputer:{computer} \nplayer win')
    elif player < computer:
        print(f'player:{player} \ncomputer:{computer} \ncomputer win')
    else:
        print(f'player:{player} computer:{computer} \nno win')
else:
    print('see you')