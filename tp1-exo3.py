import matplotlib.colors as mcolors
import numpy as np
import matplotlib.pyplot as plt

def plotVS(plot_x, plot_f1, plot_f2, f1label = "", f2label="", xlabel = "", ylabel = ""):
    f= plt.figure(figsize=(9, 7))
    plt.tight_layout()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()
    #plt.xticks(range(1, 30))
    plt.xticks(np.linspace(0, max(max(plot_f1), max(plot_f2)), num=14))
    plt.yticks(np.linspace(0, len(plot_x), num=25, dtype=np.longfloat))
    f.tight_layout(h_pad=0.5)
    #print(plot_f1)
    plt.hist(plot_f1, bins='rice', label=f1label)
    plt.hist(plot_f2, bins='stone', label=f2label, color='c')
    #plt.plot(plot_x, plot_f1, '-k', label=f1label)
    plt.legend()
    plt.show()

def plot(plot_x, plot_f1, f1Label = "", xlabel = "", ylabel = ""):
    f= plt.figure(figsize=(9, 7))
    plt.tight_layout()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()
    #plt.xticks(range(1, 30))
    plt.xticks(np.linspace(0, max(plot_f1), num=10))
    plt.yticks(np.linspace(0, len(plot_f1), num=25, dtype=np.longfloat))
    f.tight_layout(h_pad=0.5)
    #print(plot_f1)
    plt.hist(plot_f1, bins='rice', label=f1Label)
    #plt.plot(plot_x, plot_f1, '-k', label=f1Label)
    plt.legend()
    plt.show()

def binm(p, n:int, k:int):
    """:return: Probability of having 'k' success (with proba 'p') among 'n' Bernoulli trials."""
    n = np.ulonglong(n)
    k = np.ulonglong(k)
    tmp = np.longfloat(np.math.comb(n, k)) * np.longfloat(p ** k)
    out = np.longfloat((1-p) ** (n-k))
    return tmp * out

def modelBin(p, n, simulation_amnt):
    """Modelise X. i.e. random variable that follows binomial distribution.
    simulation_amnt: number of simulation of X in modelisation (i.e. graph / histogram)"""
    
    plot_x = np.linspace(0, n, num=simulation_amnt)
    plot_f1 = np.array([binm(p, n, k) for k in plot_x])
    plot(plot_x, plot_f1, "Binomial Distrib", "bins value - proba of success", "frequency per value")


def binY(lbda, n, k):
    """:return: binomial distrib with p:=lambda/n"""
    return binm(lbda/n, n, k)

def modelBinY(lbda, n, simulation_amnt):
    """Modelise Y. i.e. random variable that follows binomial distribution with p:=lbda/n"""
    p = np.longfloat(lbda/n)
    print("proba p =", p)
    plot_x = np.linspace(0, n, num=simulation_amnt)
    plot_f1 = np.array([binm(p, n, k) for k in plot_x])
    plot(plot_x, plot_f1, "Binomial Distrib with p:= $\lambda/n$", "bins value - proba of success", "frequency per value")

def modelBinX_VS_Y(px, lbda, n, simulation_amnt):
    p = np.longfloat(lbda/n)
    plot_x = np.linspace(0, n, num=simulation_amnt)
    plot_f1 = np.array([binm(px, n, k) for k in plot_x])
    plot_f2 = np.array([binm(p, n, k) for k in plot_x])
    plotVS(plot_x, plot_f1, plot_f2, "$B(n, p)\ $ (for $p=0.5$)", "$B(n, p_n := \lambda/n)$", "Proba of k success", "frequency per value")
    

if __name__ == '__main__':
    #sn, p, simul_amnt = 50, 
    n, lbda, simul_amnt = 50, 2, 10000
    """ modelBin(0.5, n, simul_amnt)
    modelBinY(lbda, n, simul_amnt) """
    modelBinX_VS_Y(0.5, lbda, n, simul_amnt)
