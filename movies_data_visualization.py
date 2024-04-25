import matplotlib.pyplot as plt
import pandas as pd


def plot_budget_vs_revenue(csv_file_path, save_plot_path=None):
    df = pd.read_csv(csv_file_path)

    df_relevant = df[
        [
            'title', 'release_date', 'budget', 'revenue'
        ]
    ]

    df_relevant = (
        df_relevant
        .loc[df_relevant['release_date'] > '1990']
        .copy()
    )

    # df_recent = (
    #     df_relevant
    #     .set_index('revenue')
    #     .sort_index()
    #     .copy()
    # )

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.plot(
        df_relevant['budget'] / 1e6,
        df_relevant['revenue'] / 1e6,
        '.',
        color='black'
    )

    ax.set_xlabel('Budget (in millions)')
    ax.set_ylabel('Revenue (in millions)', rotation=0, ha='right', ma='left')

    max_revenue_movie = df_relevant.loc[df_relevant['revenue'].idxmax()]
    max_budget_movie = df_relevant.loc[df_relevant['budget'].idxmax()]

    ax.plot(
        max_revenue_movie['budget'] / 1e6,
        max_revenue_movie['revenue'] / 1e6,
        'o',
        color='red',
        markersize=8,
        label=f'Highest Revenue: {max_revenue_movie["title"]}'
    )

    ax.plot(
        max_budget_movie['budget'] / 1e6,
        max_budget_movie['revenue'] / 1e6,
        'o',
        color='blue',
        markersize=8,
        label=f'Highest Budget: {max_budget_movie["title"]}'
    )

    x_offset = 4
    y_offset = 2
    ax.text(
        max_revenue_movie['budget'] / 1e6 + x_offset,
        max_revenue_movie['revenue'] / 1e6 + y_offset,
        f'\n Highest Revenue movie: {max_revenue_movie["title"]}\n'
        f'"{int(max_revenue_movie["revenue"] / 1e6):,}"',
        color='red',
        fontsize=8,
        va='top',
        ha='center'
    )

    ax.text(
        max_budget_movie['budget'] / 1e6 + x_offset,
        max_budget_movie['revenue'] / 1e6 + y_offset,
        f'\n Highest Budget movie: \n{max_budget_movie["title"]}\n'
        f'"{int(max_budget_movie["budget"] / 1e6):,}"',
        color='blue',
        fontsize=8,
        va='top',
        ha='center'
    )

    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().yaxis.set_label_coords(-0.03, 1)
    plt.title('The Relationship Between Budget and Revenue')

    if save_plot_path:
        plt.savefig(save_plot_path, dpi=120, bbox_inches='tight')

    plt.show()


# Example usage:
plot_budget_vs_revenue('tmdb_5000_movies.csv', 'plot.png')
