import matplotlib.pyplot as plt
from data_manager import load_ratings


def show_rating_chart():
    """Display average rating for each song."""

    df = load_ratings()

    if df.empty:
        return False

    df["Rating"] = pd_to_numeric(df["Rating"])

    df = df.dropna(subset=["Rating"])

    if df.empty:
        return False

    song_avg = (
        df.groupby("Song")["Rating"]
        .mean()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(10, 5))

    plt.bar(
        song_avg.index,
        song_avg.values
    )

    plt.title("Average Rating by Song")
    plt.xlabel("Song")
    plt.ylabel("Average Rating")

    plt.ylim(0, 5)

    plt.xticks(
        rotation=35,
        ha="right"
    )

    plt.tight_layout()
    plt.show()

    return True


def show_genre_chart():
    """Display average rating by genre."""

    df = load_ratings()

    if df.empty:
        return False

    df["Rating"] = pd_to_numeric(df["Rating"])

    df = df.dropna(subset=["Rating"])

    if df.empty:
        return False

    genre_avg = (
        df.groupby("Genre")["Rating"]
        .mean()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(8, 5))

    plt.bar(
        genre_avg.index,
        genre_avg.values
    )

    plt.title("Audience Preference by Genre")
    plt.xlabel("Genre")
    plt.ylabel("Average Rating")

    plt.ylim(0, 5)

    plt.xticks(
        rotation=30,
        ha="right"
    )

    plt.tight_layout()
    plt.show()

    return True


def pd_to_numeric(series):
    """Safely convert values to numeric."""

    import pandas as pd

    return pd.to_numeric(
        series,
        errors="coerce"
    )