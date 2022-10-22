from random import randint


def checking_scores(score: int): return score > 75


def MAIN():
    scores = [randint(0, 100) for _ in range(101)]

    print(list(filter(checking_scores, scores)))
    print(list(filter(lambda score: score > 75, scores)))


MAIN()
