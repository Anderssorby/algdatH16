from sys import stdin, stderr


def pop_best(Q, nm, pm):
    best = Q[0]
    for i in Q:
        for e in nm[i]:
            if e == 1:
                if pm[best] < pm[i]:
                    best = i

    Q.remove(best)
    return best

def path(pi):
    # print(pi)
    p = [str(n-1)]
    parent = pi[-1]
    while parent != -1:
        p.append(str(parent))
        parent = pi[parent]
    p.reverse()
    return "-".join(p)
            

def best_path(nm, prob):
    # SKRIV DIN KODE HER
    # djikstra
    # Q = nm's
    # S = []
    pi = [-1 for i in range(n)]
    Q = [i for i in range(n)]
    pm = [0 for _ in range(n)]
    pm[0] = prob[0]
    i = 0
    while Q:
       # start in 0
       # S.append(i)
       for j, e in enumerate(nm[i]):
            if e == 1:
                relax_prob(i, j, prob, pm, pi)
       i = pop_best(Q, nm, pm)
    # print(pm)
    return path(pi)




def relax_prob(i, j, prob, pm, pi):
    # print("relaxing", pm[j])
    if pm[j] < pm[i] * prob[j]:
        pm[j] = pm[i] * prob[j]
        pi[j] = i
        # print("relaxed (", i, j, ") to", pm[j])
        # this is a better path so far (i to j)



n = int(stdin.readline())
probabilities = [float(x) for x in stdin.readline().split()]
neighbour_matrix = []
for line in stdin:
    neighbour_row = [0] * n
    neighbours = [int(neighbour) for neighbour in line.split()]
    for neighbour in neighbours:
        neighbour_row[neighbour] = 1
    neighbour_matrix.append(neighbour_row)
print (best_path(neighbour_matrix, probabilities))
