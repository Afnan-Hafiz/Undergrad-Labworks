#6 FINAL
import random

def playRockPaperScissor(rounds):
    myscore = 0
    compscore = 0
    a = "rock"
    b = "paper"
    c = "scissor"
    win = ""
    prep = ""
    for i in range(rounds):
        m = input("Enter your choice (rock/paper/scissor): ").lower()
        x = random.choice([a, b, c])
        print("Computer:", x)

        if m == a and x == b:
            compscore += 1
        elif m == a and x == c:
            myscore += 1
        elif m == b and x == c:
            compscore += 1
        elif m == b and x == a:
            myscore += 1
        elif m == c and x == b:
            compscore += 1
        elif m == c and x == a:
            myscore += 1

    if compscore > myscore:
        win += "Computer"
        prep += "have"
    elif compscore < myscore:
        win += "You"
        prep += "has"
    else:
        return "It's a tie!"

    return f"Your score: {myscore}\nComputer's score: {compscore}\n{win} {prep} won the game!"

N = int(input("Number of rounds: "))
print(playRockPaperScissor(N))