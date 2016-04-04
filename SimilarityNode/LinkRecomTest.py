__author__ = 'zhan'

import Heap
from Node import Node

def link_recom(G, num, target):
    INFINITY = 100
    def sim(d1, d2):
        return 1/float(d1+d2-1)

    s = [0.0]*num;
    # for i in xrange(0, num):
    #     s[i] = 0.0

    degree = []
    for row in G:
        deg = 0.0
        for i in row:
            deg = deg + i
        degree.append(deg)

    H = [Node(-1, -1)]
    dist = [INFINITY]*num
    # for j in xrange(0, num):
    #     dist[j] = INFINITY
    threshold = 0.05

    v = target
    s[v]=1
    dist[v] = 0
    v0 = Node(v, 0)
    Heap.insert(H, v0)

    while len(H) > 1:
        v = Heap.get_min(H).name
        A = G[v]
        neighbor = [i for i in range(0, len(A)) if A[i] != 0.0]
        for k in neighbor:
            if dist[k]>dist[v]+G[v][k]:
                dist[k] = dist[v]+G[v][k]
                node_k = Node(k, dist[k])
                s[k] = s[v]*sim(degree[v], degree[k])
                if node_k not in H and s[k] >= threshold:
                    Heap.insert(H, node_k)

    # print 'sucessful'
    # print s
    # print H
    #print dist

    similarity ={}
    count = 0
    for i in s:
        similarity[count]=i
        count = count + 1

    sorted_sim = sorted(similarity.items(),key=lambda e:e[1], reverse=True)
    print "probability of relationship with target %s" % target
    print sorted_sim[1:]
    # target_v = target
    # r = G[target_v]
    # neib = [i for i in range(0, len(r)) if r[i]!=0.0]
    # neib.append(target_v)
    # print neib
    # recom = [y for y in sorted_sim if y[0] not in neib]

    # print recom

if __name__ == '__main__':
    data_file = open('D:\Python Project\LinkRecom\data.txt')
    # the number of nodes
    size = 10
    G = [([0.0]*size) for i in range(size)]

    while True:
        line = data_file.readline()
        data = line.strip('\n').split('  ')
        if len(data) == 3:
            G[int(data[0])][int(data[1])] = float(data[2])
        if not line:
            break

    link_recom(G, 10, 0)
    link_recom(G, 10, 2)
    link_recom(G, 10, 1)
    link_recom(G, 10, 3)



