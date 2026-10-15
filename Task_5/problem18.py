
# Problem 18: The Minion Game
# HackerRank Link: https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    kevin = 0
    stuart = 0
    vowels = "AEIOU"
    length = len(string)

    for i in range(length):
        if string[i] in vowels:
            kevin += length - i
        else:
            stuart += length - i

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
