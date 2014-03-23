import matplotlib.pyplot as plt


def plot(filename):
    fig, axes = plt.subplots()
    a = [float(l.strip()) for l in open(filename).readlines()]
    axes.plot(range(len(a)), a)
    fig.show()
    return fig, axes
