
def dist(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2 )**0.5


def tableau_dist(a, L):
    tab = []
    for x in L:
        if dist(a,x) != 0:
            tab.append((x, dist(a,x)))
    return tab

def knn(k, a, L):
    tab = tableau_dist(a, L)
    tab.sort(key=lambda x: x[1])
    final_tab = []
    for i in range(k):
        final_tab.append(tab[i][0])
    return final_tab


