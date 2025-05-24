import random
import time

class Game:
    def __init__(self):
        self.draw = []
        self.point = 0

    def when_hit(self, card:list, card_value:dict):
        hit = random.choice(card)
        self.draw.append(hit)
        card.remove(hit)
        self.point += card_value[hit]
        return hit

def judge(pp:int, np:int):
    if pp > 21:
        if np > 21:
            return None
        else:
            return False
    else:
        if np > 21:
            return True
    
    if (21 - pp) < (21 - np):
        return True
    elif (21 - pp) > (21 - np):
        return False
    else:
        return None

def print_table(pd:list, nd:list):
    print(f"{'-' * 23}")
    print("Opponent's card:")
    for i in nd:
        print(f'[{i}] ',end = ' ')
    print('\n')
    print("Your card:")
    for i in pd:
        print(f'[{i}] ',end = ' ')
    print('')
    print(f"{'-' * 23}")
    return

def npc_calculate(npc_point:int, card_value:dict, pfc:str, card:list):
    safe = 0
    danger = 0
    probability = random.random()
    actual_p = 0.0
    
    if npc_point + card_value[pfc] > 21:
        danger += 1
    else:
        safe += 1

    for i in card:
        if npc_point + card_value[i] > 21:
            danger += 1
        else:
            safe += 1

    actual_p = float(safe) / float(safe + danger)

    if probability <= actual_p:
        return True
    else:
        return False

def new_round():
    card = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    card_value = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13}
    
    player = Game()
    npc = Game()

    player.when_hit(card, card_value)
    npc.when_hit(card, card_value)
    nfk = npc.draw[0]
    npc.draw[0] = '*'
    print("'The initial deal is complete.'")

    action = ''
    npc_action = True

    while card:
        print_table(player.draw, npc.draw)
        if action != 'stand':
            action = input("'Hit or stand?' ")
            if action.lower() != 'stand':
                hit = player.when_hit(card, card_value)
                print('...')
                time.sleep(2)
                print(f"'Here is your card:[{hit}]'")
        

        time.sleep(2)

        if not card:
            break

        if npc_action:
            npc_action = npc_calculate(npc.point, card_value, player.draw[0],card)
            if npc_action:
                print('...')
                time.sleep(2)
                print("'I choose to hit.'")
                hit = npc.when_hit(card, card_value)
                print('...')
                time.sleep(2)
                print(f"'Here is my card:[{hit}]'")
            else:
                print('...')
                time.sleep(2)
                print("'I choose to stand.'")
        else:
            print("'I stand.'")

        time.sleep(2)
        print('')

        if npc_action == False and action == 'stand':
            break
    
    print("'Let's flip the cards and see the result!'")
    npc.draw[0] = nfk
    print_table(player.draw, npc.draw)
    print(f"Your points: {player.point}    Opponent's points: {npc.point}")
    return judge(player.point, npc.point)
    



if __name__ == '__main__':
    print("'Hello there, do you want to play a game?'")
    act = input('Yes or No: ')
    if act.lower() == 'yes':
        print("'Nice! I like people who get straight to the point.'")
    elif act.lower() == 'no':
        print("'Relax, it'll be over before you know it!'")
    else:
        print("'You don't seem to have made up your mind, so I'll take that as a yes!'")

    time.sleep(2)
    print("'If you're still not familiar with the rules, I suggest going back to the website and reading through them again.'")
    time.sleep(2)
    print("'Of course, playing a few rounds is also a great way to get the hang of it!'")
    time.sleep(2)

    print("\n'Alright then, let's begin!'")
    
    while True:
        result = new_round()
        print("'The winner is ...'")
        time.sleep(3)
        if result == None:
            print("'Nobody!'")
        elif result == True:
            print("'You!'")
        else:
            print("'Me!'")

        print('')

        time.sleep(2)
        print("'That was fun. Want to play again?'")
        act = input('Enter yes to start next round, or enter anything to end: ')
        if act.lower() != 'yes':
            print("'See you!'")
            break

