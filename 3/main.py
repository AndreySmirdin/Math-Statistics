import math
import random
import matplotlib.pyplot as plt

THETA = 50
EXPERIMENTS = 1000
MAX_K = 180

def estimate_parameter(k):
    sum = 0
    for _ in range(EXPERIMENTS):
        sum += math.pow(random.uniform(0, THETA), k)
    sum /= EXPERIMENTS
    return pow((k + 1) * sum, 1 / k)


if __name__ == "__main__":
    results = []
    for k in range(1, MAX_K):
        val = estimate_parameter(k)
        print(val)
        results.append((THETA - val) * (THETA - val))

    plt.plot([i for i in range(1, MAX_K)], results)
    plt.savefig('result.png')
    plt.show()
