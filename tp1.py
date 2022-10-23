import numpy as np
import math
from math import comb

def bt(p, nb=1):
    """Bernoulli Trials, where p(1) := p, p(0) := 1-p"""
    if nb < 1: return None
    if p < 0 or p > 1: raise ValueError(f"function bt, Probability p={p} is not in [0, 1].")
    dist = [1-p, p]
    return np.random.choice(2, 1, p=dist)[0] if nb == 1 else np.random.choice(2, nb, p=dist)

def countWins(p, nb):
    wins = np.longfloat(bt(p, nb).sum())
    return (wins, np.longfloat(nb)-wins)

def testProba_simulation():
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

# sums of n independant Bernoulli trials => === binomial distribution with param B(n, p)

def binomial(n, p, k):
    print(n, p, k)
    """n = np.ulonglong(n)
    p = np.longfloat(p)
    k = np.ulonglong(k)"""
    tmp = (np.math.comb(n, k))
    tmp1: np.longfloat = tmp * (p ** n)
    tmp2: np.longfloat = np.longfloat((1-p) ** (n-k))
    tmp3:np.longfloat  = tmp1 * tmp2
    print("tmp3 = ", tmp3)
    return tmp3 #np.longlong(tmp) * tmp3


def expected_value(P, ys):
    """ P: probability distribution of random variable to compute exp value from 
        ys: range of random variable (i.e. != values) """
    return np.array([P(yi)*yi for yi in ys], dtype=np.longfloat).sum()


def countWinsBin(n, p):
    ys = np.arange(n+1, dtype=np.ulonglong)
    def binml(yi): return binomial(n, p, yi)
    exp_value = expected_value(binml, ys)
    #np.array(([binomial(n, p, yi)*yi for yi in ys]).sum())
    return exp_value

if __name__ == "__main__":
    print("")
    try:
        #testProba_simulation()
        n = 1000
        p = 0.25
        print(countWinsBin(n, p))
    except ValueError as ve: print(f"Caught Exception:\n   ", "ValueError:", ve)

    print("")
