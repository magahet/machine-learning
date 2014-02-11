import matplotlib.pyplot as plt


def plot_multiple(results_list, x_field, y_field, y2_field=None, title_field='', x_label='', y_label='', show=False):
    f, axarr = plt.subplots(len(results_list), sharex=True)
    for num, results in enumerate(results_list):
        x = [r[x_field] for r in results]
        y = [r['results'][y_field] for r in results]
        axarr[num].plot(x, y)
        if y2_field:
            y2 = [r['results'][y2_field] for r in results]
            axarr[num].plot(x, y2, color='r')
        if title_field:
            title = results[0].get(title_field)
            axarr[num].set_title(title)
    f.text(0.5, 0.04, x_label, ha='center', va='center')
    f.text(0.06, 0.5, y_label, ha='center', va='center', rotation='vertical')
    if show:
        f.show()
    return f, axarr


def plot_result(results, x_field, y_field, title='', show=False):
    fig, axes = plt.subplots()
    x = [r[x_field] for r in results]
    y = [r['results'][y_field] for r in results]
    axes.scatter(x, y)
    axes.set_xlabel(x_field)
    axes.set_ylabel(y_field)
    if title:
        axes.set_title(title)
    if show:
        fig.show()
    return fig, axes
