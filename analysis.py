import numpy as np
import pandas as pd
from data_manager import load_ratings


def get_clean_data():
    """Return cleaned rating data."""

    df = load_ratings()

    if df.empty:
        return df

    df["Rating"] = pd.to_numeric(
        df["Rating"],
        errors="coerce"
    )

    df = df.dropna(subset=["Rating"])

    return df


def get_summary():
    """Generate complete audience preference summary."""

    df = get_clean_data()

    if df.empty:
        return "No rating records available."

    ratings = df["Rating"].to_numpy()

    overall_average = np.mean(ratings)
    highest_rating = np.max(ratings)
    lowest_rating = np.min(ratings)

    song_avg = (
        df.groupby("Song")["Rating"]
        .mean()
        .sort_values(ascending=False)
    )

    genre_avg = (
        df.groupby("Genre")["Rating"]
        .mean()
        .sort_values(ascending=False)
    )

    artist_avg = (
        df.groupby("Artist")["Rating"]
        .mean()
        .sort_values(ascending=False)
    )

    best_song = song_avg.index[0]
    best_song_rating = song_avg.iloc[0]

    worst_song = song_avg.index[-1]
    worst_song_rating = song_avg.iloc[-1]

    best_genre = genre_avg.index[0]
    best_genre_rating = genre_avg.iloc[0]

    best_artist = artist_avg.index[0]
    best_artist_rating = artist_avg.iloc[0]

    total_ratings = len(df)
    total_songs = df["Song"].nunique()
    total_members = df["Member"].nunique()
    total_artists = df["Artist"].nunique()
    total_genres = df["Genre"].nunique()

    return (
        "AUDIENCE PREFERENCE ANALYSIS\n"
        "=============================\n\n"

        f"Total ratings: {total_ratings}\n"
        f"Total unique songs: {total_songs}\n"
        f"Total audience members: {total_members}\n"
        f"Total artists: {total_artists}\n"
        f"Total genres: {total_genres}\n\n"

        f"Overall average rating: "
        f"{overall_average:.2f}/5\n"

        f"Highest rating given: "
        f"{highest_rating:.1f}/5\n"

        f"Lowest rating given: "
        f"{lowest_rating:.1f}/5\n\n"

        f"Highest-rated song: "
        f"{best_song} ({best_song_rating:.2f}/5)\n"

        f"Lowest-rated song: "
        f"{worst_song} ({worst_song_rating:.2f}/5)\n\n"

        f"Preferred genre: "
        f"{best_genre} ({best_genre_rating:.2f}/5)\n"

        f"Top artist: "
        f"{best_artist} ({best_artist_rating:.2f}/5)"
    )


def get_genre_analysis():
    """Return genre-wise rating analysis."""

    df = get_clean_data()

    if df.empty:
        return pd.DataFrame()

    return (
        df.groupby("Genre")
        .agg(
            Average_Rating=("Rating", "mean"),
            Number_of_Ratings=("Rating", "count")
        )
        .sort_values(
            "Average_Rating",
            ascending=False
        )
    )


def get_song_analysis():
    """Return song-wise rating analysis."""

    df = get_clean_data()

    if df.empty:
        return pd.DataFrame()

    return (
        df.groupby("Song")
        .agg(
            Average_Rating=("Rating", "mean"),
            Number_of_Ratings=("Rating", "count")
        )
        .sort_values(
            "Average_Rating",
            ascending=False
        )
    )