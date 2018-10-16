import math
import random

import matplotlib.pyplot as plt

THETA = 10
EXPERIMENTS = 100
MAX_K = 100
SERIES = 100


def print(a):
    pass

def estimate_uniform(k):
    res = sum([random.uniform(0, THETA) ** k for _ in range(EXPERIMENTS)]) / EXPERIMENTS
    return ((k + 1) * res) ** (1 / k)


def estimate_exp(k):
    res = sum([random.expovariate(THETA) ** k for _ in range(EXPERIMENTS)]) / EXPERIMENTS
    return (math.factorial(k) / res) ** (1 / k)


def do(estimate_param, plot_name):
    results = []
    for k in range(1, MAX_K):
        deviation = sum([(THETA - estimate_param(k)) ** 2 for _ in range(SERIES)])
        results.append((deviation / SERIES) ** 0.5)

    plt.clf()
    plt.plot([i for i in range(1, MAX_K)], results)
    plt.savefig(plot_name)


if __name__ == "__main__":
    print(3, 4)
    do(estimate_uniform, 'uniform.png')
    do(estimate_exp, 'exponential.png')
