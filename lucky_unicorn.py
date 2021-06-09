from random import choice
prize_money = 0

valid = False 
while not valid:
    try:
        dollars = int(input("how much are you ging to put into the game?\n"))
        if 0 < dollars <= 10:
            valid = True
        else:
            print("please use whole numbers between 1 and 10")
    except ValueError:
        print("please use whole numbers between 1 and 10")
tokens = []
horse_num = 500
zebra_num = 350
donkey_num = 100
unicorn_num = 1
for i in range(horse_num):
    tokens.append("horse")

for i in range(zebra_num):
    tokens.append("zebra")

for i in range(unicorn_num):
    tokens.append("unicorn")

for i in range(donkey_num):
    tokens.append("donkey")

    dollars -= 1
    token = choice(tokens)

    rewards = {"horse":0.5,
                "zebra":0.5,
                "donkey":0,
                "unicorn": 100}
    reward = rewards[token]

    if token == "horse" or "zebra":
        print(f"congradulations you got a {token} \n you win a ${reward} as a prize")

    if token == "donkey":
        print(f'oh no you got {token} \n you win {reward} as a prize')

    if token == "unicorn":
        print(f'jackpot!!!, you got {token} \n you win {reward} as a prize')
    
    prize_money += reward
    dollars += reward
    print(f"your current winnings:{prize_money}. money left: ${dollars}")
    replay = input("press enter to play again\n type exit to cash out\n")
    if replay == "exit" or dollars < 0.5:
        break

print("see you next time ^~^")