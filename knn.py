
def dist(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2 )**0.5


def knn(a,L):
    b_min = L[0]
    dist_min = dist(a, L[0])
    for x in L[1:]:
        dist_temp = dist(a, x)
        if dist_temp < dist_min:
            dist_min = dist_temp
            b_min = x
    return b_min


