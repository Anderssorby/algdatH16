#!/usr/bin/python3

from sys import stdin


def cut_rod(p, n):
    if n == 0:
        return 0
    q = -1

    i = 0
    while i < n:
        q = max(q, p[i] + cut_rod(p, n-i-1))
        i += 1
    print("n =", n, "q =", q)
    return q


def cut_rod_memo(p, n):
    r = [-1]*(n+1)
    return cut_rod_memo_aux(p, n, r)


def cut_rod_memo_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    q = 0
    if n != 0:
        q = -1
        i = 0
        while i < n:
            q = max(q, p[i] + cut_rod_memo_aux(p, n-i-1, r))
            i += 1
    r[n] = q
    print(r,"n =",n)
    return q


def bottom_up_cut_rod(p, n):
    r = [-1]*(n+1)
    r[0] = 0
    j = 1
    while j <= n:
        q = -1
        i = 0
        while i < j:
            q = max(q, p[i] + r[j-i-1])
            i += 1
        r[j] = q
        print("q =", q, "j =", j)
        j += 1
    print(r)
    return r[n]


def back_pack(v, w, W, exclude=[]):
    V = 0
    j = 0
    n = len(v)
    while j < n:
        if j not in exclude:
            if w[j] <= W:
                V = max(V, v[j] + back_pack(v, w, W-w[j], exclude+[j]))
        j += 1
    return V


def max_value(widths, heights, values, paper_width, paper_height):
    # set up
    r = [[-1] * (paper_height+1) for _ in range(paper_width+1)]
    r[0][0] = 0
    print(r)
    # memoization
    # if r[paper_width][paper_height] >= 0:
    #     return r[paper_width][paper_height]
    # cut out bills until you cannot
    # Then see if your solution is better than the last
    # cutting out one bill then the problem is reduced to 
    # findig the best value of the remainder of the paper
    # The remainder of the paper is the


    n = len(values)
    for i in range(n):
        
        w = widths[i]
        h = heights[i]
        v = values[i]

        r[w][h] = max(r[w][h], v)

    for w in range(paper_width+1):
        for h in range(paper_height+1):
            


    q = 0
    i = 0
    if paper_width != 0 and paper_height != 0:
        while i < n:
            # select a bill
            w = widths[i]
            h = heights[i]
            v = values[i]
            # Place it into the paper either standing or laying
            # Standing
            if w <= paper_width and h <= paper_height:
                # we have a new paper with a section cut out
                # expand as many times as possible in one direction
                # we get possibly three new papers 

                # v1 = max_value_aux(widths, heights, values, w, paper_height-h, r)
                # v2 = max_value_aux(widths, heights, values, paper_width-w, h, r)
                # v3 = max_value_aux(widths, heights, values, paper_width-w, paper_height-h, r)
                
                # q = max(q, v + v1 + v2 + v3)
            
            if w <= paper_height and h <= paper_width:
                # laying
                # v1 = max_value_aux(widths, heights, values, h, paper_height-w, r)
                # v2 = max_value_aux(widths, heights, values, paper_width-h, w, r)
                # v3 = max_value_aux(widths, heights, values, paper_width-h, paper_height-w, r)
                
                # q = max(q, v + v1 + v2 + v3)

            i += 1 
    r[paper_width][paper_height] = q
    return q


def place_bill(widths, heights, values, paper_width, paper_height):
    pass



def max_value_aux2(widths, heights, values, paper_width, paper_height, r): 
    
    q = 0
    i = 0
    n = len(values)
    if paper_width != 0 or paper_height != 0:
        while i < n:
            h = heights[i]
            w = widths[i]
            q = max(q, values[i] + max_value_aux(widths, heights, values, paper_width-w, paper_height-h, r))
            
            i += 1
    r[n] =  q
    return q


    


def main():
    widths = []
    heights = []
    values = []
    for triple in stdin.readline().split():
        dim_value = triple.split(':', 1)
        dim = dim_value[0].split('x', 1)
        width = int(dim[0][1:])
        height = int(dim[1][:-1])
        value = int(dim_value[1])
        widths.append(int(width))
        heights.append(int(height))
        values.append(int(value))
    for line in stdin:
        paper_width, paper_height = [int(x) for x in line.split('x', 1)]
        print((max_value(widths, heights, values, paper_width, paper_height)))


if __name__ == "__main__":
    main()
