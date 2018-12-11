import matplotlib.pyplot as plt
import numpy as np

A = 1
C = 1 / (2 * A + 2 * np.exp(-A))


def generate1():
    # Обратная функция
    # F(x) = ce^{-x}, x <= -A
    #      = ce^{-A} + cx, -A < x < A
    #      = 1 - ce^{-x}, x >= A
    # G(y) = ln(y / C), y <= ce^{-A}
    #      = y/c - e^{-A}, ce^{-A} < y < ce^{-A} + 2cA
    #      = ln(c / (1 - y)), y >= ce^{-A} + 2cA
    y = np.random.uniform(0, 1)
    if y < C * np.exp(-A):
        return np.log(y / C)
    if y > C * np.exp(-A) + 2 * C * A:
        return np.log(C / (1 - y))
    return y / C - np.exp(-A)


def generate2():
    k = np.random.uniform(0, 1)
    if C * np.exp(-A) < k < C * np.exp(-A) + 2 * C * A:
        return np.random.uniform(-A, A)
    x = np.random.exponential(1)
    while x < A:
        x = np.random.exponential(1)
    return x * (1 if np.random.uniform() > 0.5 else -1)


if __name__ == "__main__":
    l1 = [generate1() for _ in range(1000)]
    l2 = [generate2() for _ in range(1000)]
    l1.sort()
    l2.sort()
    print(l1)
    plt.plot(range(1000), l1)
    plt.plot(range(1000), l2)
    plt.savefig('123.png')
