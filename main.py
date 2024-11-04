import random

def RollDice():
    number  = random.randint(1,6)
    print(number)

def main():
    while True:
        reroll = input("Do You want to roll dice? (y/n)")

        if reroll not in["yes",'y']:
            print("Thanks for playing!")
            break
        RollDice()

if __name__ == "__main__":
    main()