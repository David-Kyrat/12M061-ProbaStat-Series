from numpy import random
from copy import deepcopy


def loi_binom(n, p):
    return random.binomial(n=n, p=p)


def loi_bernouli(p):
    return random.binomial(n=1, p=p)


def RS(J):
    # On prend la longueur de la liste
    n = len(J)
    # On défini à quel endroit on va 'couper' le tas
    tronc = loi_binom(n, 1 / 2)
    # On crée les 2 paquets obtenus par la séparation du tas
    #paquet_1 = J[:tronc]
    paquet_1 = [J[i] for i in range(tronc)]

    # paquet_2 = [J[i] for i in range(tronc, n)]
    paquet_2 = J[tronc:n]

    # On crée notre liste qui permettra de stocker la liste finale
    R = []
    # Tant que les paquets ne sont pas vides, on boucle
    while len(paquet_1) != 0 and len(paquet_2) != 0:
        # On définit la probabilité de prendre une carte du paquet_1
        p = len(paquet_1) / (len(paquet_1) + len(paquet_2))
        # Si la loi de bernouli donne 0, c'est que la carte appartient au premier paquet, sinon, la carte appartient au deuxième paquet.
        # En effet, on a n_1/n_1+n_2 + n_2/n_1+n_2 = n_1+n_2/n_1+n_2 = 1. Donc cela suit une loi de bernouli.
        if loi_bernouli(p) == 0:
            # R.append(paquet_1[0])
            # paquet_1.pop(0)
            R.append(paquet_1.pop(0))
        else:
            # R.append(paquet_2[0])
            # paquet_2.pop(0)
            R.append(paquet_2.pop(0))

    # Si un des deux paquets n'est pas vide, on va ajouter tous les éléments restants dans le résultat.
    R += paquet_1 if (len(paquet_1) != 0) else paquet_2

    """while (len(paquet_1) != 0):
        R.append(paquet_1[0])
        paquet_1.pop(0)
    while (len(paquet_2) != 0):
        R.append(paquet_2[0])
        paquet_2.pop(0)"""
    # On retourne le résultat
    return R


"""def Trajectoire(JO, T):
    # On initialise une liste vide permettant de stocker le résultat.
    result = []
    # On ajoute JO dans notre liste vide
    result.append(JO)
    # On ajoute ensuite successivement J1 = RS(JO), J2 = RS(J1).... JT = RS(JT-1)
    for i in range(1, T + 1):
        result.append(RS(result[i-1]))
    # On retourne le résultat
    return result
"""
def Trajectoire(J0, T):
    # On initialise une liste vide permettant de stocker le résultat.
    # On ajoute JO dans notre liste vide
    result = [J0]
    # On ajoute ensuite successivement J1 = RS(JO), J2 = RS(J1).... JT = RS(JT-1), qu'on retourne après quit
    for i in range(0, T):
        result.append(RS(result[i]))

    return result


if __name__ == "__main__":
    n = 5
    J = list(range(n))
    print("J =\t", J)
    res = RS(J)
    print("RS(J):\t", res)

    traj = Trajectoire(J, n)
    print("\nTrajectoire(J):")
    for row in traj: print(f"\t{row}")
    print(f"Dim:\t{len(traj)} x {len(traj[0])}")

