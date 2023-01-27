import random
import re


def dice_roller():
    print("What do I need to roll? ((amount)D(size)+(modifier) ex. 2D6+2)")
    print('To exit the loop write "exit"')
    allowed_dice = [2,3,4,6,8,10,12,20,100]
    input_dice = input("Roll: ")
    decode_dice = re.split(r'd|D|-|[+]', input_dice)
    if len(decode_dice) != 3:
        decode_dice.insert(2, "0")
    try:
        if input_dice == "exit":
            active = False
        if int(decode_dice[1]) not in allowed_dice:
            raise Exception(f"Invalid dice size picked try one of those {allowed_dice}")
        dice_size = list(range(1, int(decode_dice[1]) + 1))
        rolls = random.choices(dice_size ,k=int(decode_dice[0]))
        print(sum(rolls) + int(decode_dice[2]))
    except ValueError:
        print("Sorry the dice code you provided is incorrect. Try something like ex. 2D6+6")


dice_roller()