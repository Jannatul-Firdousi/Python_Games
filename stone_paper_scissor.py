import random


def sps(c, m):
    if c == m:
        return None
    elif c == "paper" and m == "scissor":
        return True
    elif c == "stone" and m == "paper":
        return True
    elif c == "scissor" and m == "stone":
        return True
    else:
        return False


choice = ("stone", "paper", "scissor")
comp = random.randint(0, 2)
comp = choice[comp]
mine = input("Enter stone/paper/scissor!!\n")

win = sps(comp, mine)
print(f"You chose {mine} and the computer chose {comp}:")
if win is None:
    print("Match is drawn!")
elif win:
    print("You won!")
else:
    print("You loose!")
