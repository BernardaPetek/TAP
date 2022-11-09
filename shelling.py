import itertools


def shelling(T):
    tsequence = []
    T1 = []

    for i in range(len(T)):
        T1.append(frozenset(map(frozenset, itertools.combinations(T[i], 2))))

    available_edges = set()
    triangles = set(T1)
    tsequence.append(triangles.pop())
    available_edges.update(tsequence[0])


    while triangles:
            check = True
            for element in triangles:
                if len(element.intersection(available_edges)) == 2:
                    tsequence.append(element)
                    available_edges.update(element)
                    check = False
                    break

            if check:
                for element in triangles:
                    if len(element.intersection(available_edges)) == 1:
                        tsequence.append(element)
                        available_edges.update(element)
                        break

            triangles.remove(tsequence[len(tsequence) - 1])

    result = []
    for sets in tsequence:
        unija = list(sets)
        result.append(tuple(sorted(list(set().union(*unija)))))

    return result

def animate_shelling_sequence(T, sequence):
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation

    # Set up visualization grid
    max_val = max(max(t) for t in T)
    per_dim = int(np.sqrt(max_val))
    xs, ys = np.mgrid[:per_dim, :per_dim]
    xs = xs.reshape(max_val, 1).ravel()
    ys = ys.reshape(max_val, 1).ravel()
    coords = np.vstack([xs, ys]).T

    fig, ax = plt.subplots(figsize=(8, 8))

    def animate(t_idx):
        ax.clear()
        ax.scatter(coords[:, 0], coords[:, 1], c="k", zorder=5)

        def _plot_triangle(x, y, z, c="k", zorder=1, lw=1, fill=False):
            ax.plot([coords[x, 0], coords[y, 0]], [coords[x, 1], coords[y, 1]], c=c, zorder=zorder, lw=lw)
            ax.plot([coords[y, 0], coords[z, 0]], [coords[y, 1], coords[z, 1]], c=c, zorder=zorder, lw=lw)
            ax.plot([coords[z, 0], coords[x, 0]], [coords[z, 1], coords[x, 1]], c=c, zorder=zorder, lw=lw)
            if fill:
                ax.fill(
                    [coords[x, 0], coords[y, 0], coords[z, 0], coords[x, 0]],
                    [coords[x, 1], coords[y, 1], coords[z, 1], coords[x, 1]],
                    alpha=0.25,
                    color=c,
                )

        for t in T:
            x, y, z = t
            if t == t_idx:
                _plot_triangle(x - 1, y - 1, z - 1, c="r", zorder=3, lw=2, fill=True)
            elif t in sequence[:sequence.index(t_idx)]:
                _plot_triangle(x - 1, y - 1, z - 1, c="tab:blue", zorder=2, fill=True)
            else:
                _plot_triangle(x - 1, y - 1, z - 1, c="k", zorder=1)

    ani = FuncAnimation(
        fig, animate, frames=sequence, interval=300, repeat=False
    )
    #ani.save('animation.gif', writer='imagemagick', fps=30)
    plt.show()


if __name__ == "__main__":
    Tl = [(1, 2, 6), (1, 5, 6), (2, 3, 7), (2, 6, 7), (3, 4, 8), (3, 7, 8), (5, 6, 9), (6, 7, 11),
         (6, 9, 10), (6, 10, 11), (7, 8, 12), (7, 11, 12), (9, 10, 13), (10, 13, 14),
         (10, 11, 15), (10, 14, 15), (11, 12, 15), (12, 15, 16)]

    import random
    for _ in range(5):
        random.shuffle(Tl)
        sequence = shelling(Tl)
        print(sequence)
        animate_shelling_sequence(Tl, sequence)
