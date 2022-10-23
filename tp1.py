import numpy as np
import math

def bt(p, nb=1):
    """Bernoulli Trials, where p(1) := p, p(0) := 1-p"""
    if nb < 1: return None
    if p < 0 or p > 1: raise ValueError(f"function bt, Probability p={p} is not in [0, 1].")
    dist = [1-p, p]
    return np.random.choice(2, 1, p=dist)[0] if nb == 1 else np.random.choice(2, nb, p=dist)

def countWins(p, nb):
    wins = np.longfloat(bt(p, nb).sum())
    return (wins, np.longfloat(nb)-wins)

if __name__ == "__main__":
    print("")
    try:
        p = np.longfloat(0.25)
        n = 10000
        print("for p =", p, "and", n, "trials, we get:")
        wins, losses = countWins(p, n)
        print(f"{wins} wins and {losses} losses.")
        wPerc = np.longfloat(wins / n)
        mag = len(str(wPerc)) # magnitude
        lPerc = round(1 - wPerc, mag)
        print(f"i.e. {wPerc}% wins and {lPerc}% losses")
        distance = round(np.math.fabs(wPerc-p), mag)
        print(f"Measured probability distribution was only {distance}% away from the required one.")

    except ValueError as ve: print(f"Caught Exception:\n   ", "ValueError:", ve)

    print("")
