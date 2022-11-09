import numpy as np
import matplotlib.pyplot as plt
#import math

def plotVS(plot_x, plot_f1, plot_f2, title: str, xlabel: str, ylabel: str, f1Label: str, f2Label: str):
    """Plots two functions against each other.  
    - plot_x: the x-axis values
    - plot_f1: the y-values of the first function
    - plot_f2: the y-values of the second function
    - title: the title of the plot
    - xlabel: the label of the x-axis
    - ylabel: the label of the y-axis
    - f1Label: the label of the first function
    - f2Label: the label of the second function
    """
    
    plt.tight_layout()
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(plot_x, plot_f1, '-k', label=f1Label, linewidth=1)
    plt.plot(plot_x, plot_f2, '-b', label=f2Label, linewidth=1)
    plt.legend(prop={'size': 5})
    plt.legend(fontsize=7)
    #plt.legend()
    plt.show()

def bt(p, nb=1) -> np.ndarray:
    """Bernoulli Trials, where p(1) := p, p(0) := 1-p"""
    if nb < 1:
        return np.array([])
    if p < 0 or p > 1:
        raise ValueError(f"function bt, Probability p={p} is not in [0, 1].")
    dist = [1-p, p]
    return np.random.choice(2, 1, p=dist)[0] if nb == 1 else np.random.choice(2, nb, p=dist)


def countWins(p, nb):
    wins = np.longfloat(bt(p, nb).sum(dtype=np.longfloat))
    return (wins, np.longfloat(nb)-wins)


def testProba_simulation():
    p = np.longfloat(0.25)
    n = 10000
    print("for p =", p, "and", n, "trials, we get:")
    wins, losses = countWins(p, n)
    print(f"{wins} wins and {losses} losses.")
    wPerc = np.longfloat(wins / n)
    mag = len(str(wPerc))  # magnitude
    lPerc = round(1 - wPerc, mag)
    print(f"i.e. {wPerc}% wins and {lPerc}% losses")

    distance = round(np.fabs(wPerc-p), mag)
    print(f"Measured probability distribution was only {distance}% away from the required one.")

# sums of n independant Bernoulli trials => === binomial distribution with param B(n, p)


def binomial(n, p, k):
    tmp = np.longfloat(np.math.comb(n, k)) * np.longfloat(p ** k)
    out = np.longfloat((1-p) ** (n-k))
    return tmp * out


def expected_value(P, ys):
    """ P: probability distribution of random variable to compute exp value from 
        ys: range of random variable (i.e. != values) """
    return np.array([P(yi)*yi for yi in ys], dtype=np.longfloat).sum()

def countWinsBin(p, n):
    def binml(yi): return binomial(n, p, yi)
    return expected_value(binml, np.arange(n+1))


if __name__ == "__main__":
    print("")
    try:
        # testProba_simulation()
        n = 700
        p = 0.25
        out = countWinsBin(p, n)
        #k = 25
        #print(f"\n|| Probability of {k} success for {n} trials:", binomial(p, n, k))
        print(f"\n|| Computed Expected number of points out of {n} trials, (p = {p}) is: ", out)
        print(f"\n|| Actual Expected number of points out of {n} trials, (p = {p}) is: ", countWins(p, n)[0])
        x_plot = range(100, 1001, 100)
        plot_f1 = [countWinsBin(p, x) for x in x_plot]
        plot_f2 = [countWins(p, x)[0] for x in x_plot]

        print("f1", plot_f1)
        print("\nf2", plot_f2)

        plotVS(x_plot, plot_f1, plot_f2,
               "Expected Value of binomial distribution VS Actual sum of bernouilli trials",
               "Number of trials (n)", 
               "Number of success",
               "Expected Value of B(n, p)",
               "Sum of n Bernouilli Trials")
        plt.show()
        
    except ValueError as ve:
        print("Caught Exception:\n   ", "ValueError:", ve)

    print("")
