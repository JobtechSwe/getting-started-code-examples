import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="darkgrid")

def visualize_result(fractions, xlabel='year',ylabel='fraction [%]', title='\'distans\' used in ads Aug 15 - Sept 14'):
    
    sns.set_theme(style="darkgrid")
    df = pd.DataFrame(fractions.items(), columns=[xlabel,ylabel])
    g = sns.relplot(x=xlabel, y=ylabel, kind="line", marker='o', data=df)
    g.fig.autofmt_xdate()
    plt.title(title)
    plt.xticks(list(fractions.keys()))
    plt.show()


def visualize_histogram(fractions, xlabel='kompetens', ylabel ='Del', title = 'Kompetenser'):
    sns.set_theme(style="whitegrid")
    df = pd.DataFrame(fractions, columns = [xlabel,ylabel])
    sns.set_color_codes("pastel")
    sns.barplot(x=ylabel, y=xlabel, data=df,
            label=ylabel, color="b", orient="h")

    plt.title(title)
    sns.despine(left=True, bottom=True)

    plt.show()


def visualize_correlation_matrix(data, xlabel = 'ssyk1', ylabel = 'ssyk2'):

    df3 = pd.DataFrame(data=data)

    sns.set(font_scale=0.3)
    g = sns.clustermap(df3.corr(), center=0, cmap="vlag",
                    dendrogram_ratio=(.1, .2),
                    cbar_pos=(.02, .32, .03, .2),
                    linewidths=0.0, xticklabels=1, yticklabels=1 ,figsize=(12, 13))

    g.ax_row_dendrogram.remove()

    plt.show()