import matplotlib.pyplot as plt


def plot_multiple(results_list, x_field, y_field, y2_field=None, title_field='', x_label='', y_label='', show=False, chart_type='plot'):
    f, axarr = plt.subplots(len(results_list), sharex=True)
    for num, results in enumerate(results_list):
        x = [r[x_field] for r in results]
        y = [r['results'][y_field] for r in results]
        chart_method = getattr(axarr[num], chart_type, None)
        if chart_method:
            chart_method(x, y)
        if y2_field:
            y2 = [r['results'][y2_field] for r in results]
            chart_method = getattr(axarr[num], chart_type, None)
            if chart_method:
                chart_method(x, y2, color='r')
        if title_field:
            title = results[0].get(title_field)
            axarr[num].set_title(title)
    f.text(0.5, 0.04, x_label, ha='center', va='center')
    f.text(0.06, 0.5, y_label, ha='center', va='center', rotation='vertical')
    if show:
        f.show()
    return f, axarr


def plot_result(results, x_field=None, y_field=None, y2_field=None, x=None, title='', x_label='', y_label='', show=False, chart_type='plot'):
    fig, axes = plt.subplots()
    x = [r[x_field] for r in results] if x_field else x
    y = [r['results'][y_field] for r in results]
    chart_method = getattr(axes, chart_type, None)
    if not chart_method:
        return
    chart_method(x, y)
    if y2_field:
        y2 = [r['results'][y2_field] for r in results]
        chart_method = getattr(axes, chart_type, None)
        if chart_method:
            chart_method(x, y2, color='r')
    x_label = x_field if x_field else x_label
    y_label = y_field if y_field else y_label
    axes.set_xlabel(x_label)
    axes.set_ylabel(y_label)
    if title:
        axes.set_title(title)
    if show:
        fig.show()
    return fig, axes
