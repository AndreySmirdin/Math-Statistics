import random

import plotly.graph_objs as go
from plotly.offline import plot
from scipy.stats import chi2

GAMMA = 0.9


def generate_a(n):
    return sum([random.normalvariate(0, 1) ** 2 for _ in range(0, n)]) * (
            1 / chi2.ppf((1 - GAMMA) / 2, n) - 1 / chi2.ppf((1 + GAMMA) / 2, n))


def generate_b(n):
    return sum([random.normalvariate(0, 1) for _ in range(0, n)]) ** 2 / n


if __name__ == "__main__":
    xs = []
    ys1 = []
    ys2 = []

    for i in range(1, 2000):
        xs.append(i)
        ys1.append(generate_a(i))
        ys2.append(generate_b(i))

    plot([go.Scatter(x=xs[100:], y=ys1[100:], name="A"), go.Scatter(x=xs[100::10], y=ys2[100::10], name="B")])
