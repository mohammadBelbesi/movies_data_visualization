import seaborn as sns
import pandas as pd


def plot_pairplot(csv_file_path):
    df = pd.read_csv(csv_file_path)

    df_relevant = df[
        [
            'title', 'budget', 'revenue', 'popularity',
            'release_date', 'runtime', 'vote_average', 'vote_count'
         ]
    ]
    df_relevant = df_relevant.loc[
        (df_relevant['budget'] > 0) &
        (df_relevant['revenue'] > 0) &
        (df_relevant['vote_count'] > 100)
        ].copy()

    df_relevant['release_date'] = pd.to_datetime(df_relevant['release_date'])
    df_recent = (
        df_relevant.set_index('release_date')
        .sort_index()
        .loc['1990':]
        .copy()
    )

    sns.pairplot(df_recent)


# Example usage:
plot_pairplot('tmdb_5000_movies.csv')
