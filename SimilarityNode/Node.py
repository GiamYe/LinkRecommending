__author__ = 'zhan'


class Node:
    def __init__(self, name, dist):
        self.name = name
        self.distance = dist

    # def __str__(self):
    #     return self.name + ":" + str(self.distance)

    def __repr__(self):
        return "%s(%s)" % (self.name, self.distance)

    def __add__(self, other):
        self.distance = self.distance + other
        return self

    def __gt__(self, other):
        return self.distance > other

    def __lt__(self, other):
        return self.distance < other

if __name__ == '__main__':
    v0 = Node('V0', 14)
    v1 = Node('V1', 15)
    v0, v1 = v1, v0
    print v0
    print v0<v1
