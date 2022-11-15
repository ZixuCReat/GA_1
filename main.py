import math
import numpy as np


class Individual:
    def __init__(self):
        self.x = 0
        self.init_func = 0

    def __eq__(self, other):
        self.x = other.x
        self.init_func = other.init_func


def init_func(x):
    return math.exp(x) / x + x / math.exp(x)


def init_pop(pop, n):
    for i in range(n):
        ind = Individual()
        ind.x = np.random.uniform(0, 5)


def selection():
    rand = np.random.uniform(0,1)


def value_cal(parent_1, parent_2):
    child_1 = Individual()
    child_2 = Individual()
    child_1.x =

def mutation(pop):
    ind = np.random.choice(pop)
    ind.x = np.random.uniform(0, 5)
    ind.init_func = init_func(ind.x)


if __name__ == '__main__':
    n = input('个体数量')
    pop = []
    iter_n = 1000
    for i in range(iter_n):
