import numpy as np

def bt(p, nb=1):
    """Bernoulli Trials, where p(1) := p, p(0) := 1-p"""
    if nb < 1: return None
    dist = [1-p, p]
    return np.random.choice(2, 1, p=dist)[0] if nb == 1 else np.random.choice(2, nb, p=dist)

def countWins(p, nb):
    wins = bt(p, nb).sum()
    return (wins, nb-wins)

if __name__ == "__main__":
    print("")
    p, n = 0.75, 200
    print("for p =", 0.75, "and", n, "trials, we get:")
    wins, losses = countWins(p, n)
    print(f"{wins} wins and {losses} losses.")
    wPerc = wins/n
    lPerc = 1 - wPerc
    print(f"i.e. {wPerc}% wins and {lPerc}% losses.")

    print("")
