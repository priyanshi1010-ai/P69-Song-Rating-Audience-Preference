import os
import pandas as pd

DATA_FILE = "ratings.csv"

COLUMNS = [
    "ID",
    "Member",
    "Song",
    "Artist",
    "Genre",
    "Playlist",
    "Rating"
]


def load_ratings():
    """Load rating data from CSV file."""

    try:
        if not os.path.exists(DATA_FILE):
            df = pd.DataFrame(columns=COLUMNS)
            df.to_csv(DATA_FILE, index=False)
            return df

        df = pd.read_csv(DATA_FILE)

        # Make sure all required columns exist
        for column in COLUMNS:
            if column not in df.columns:
                df[column] = ""

        df = df[COLUMNS]

        # Convert rating safely
        df["Rating"] = pd.to_numeric(
            df["Rating"],
            errors="coerce"
        )

        return df

    except (pd.errors.EmptyDataError, pd.errors.ParserError):
        raise ValueError(
            "The ratings.csv file is empty or contains invalid data."
        )


def add_rating(member, song, artist, genre, playlist, rating):
    """Add a new rating to the CSV file."""

    df = load_ratings()

    if df.empty:
        new_id = 1
    else:
        ids = pd.to_numeric(df["ID"], errors="coerce").dropna()

        if ids.empty:
            new_id = 1
        else:
            new_id = int(ids.max()) + 1

    new_row = pd.DataFrame([{
        "ID": new_id,
        "Member": member,
        "Song": song,
        "Artist": artist,
        "Genre": genre,
        "Playlist": playlist,
        "Rating": rating
    }])

    df = pd.concat(
        [df, new_row],
        ignore_index=True
    )

    df.to_csv(DATA_FILE, index=False)


def delete_rating(record_id):
    """Delete a rating using its ID."""

    df = load_ratings()

    original_count = len(df)

    df = df[
        df["ID"].astype(str) != str(record_id)
    ]

    if len(df) == original_count:
        return False

    df.to_csv(DATA_FILE, index=False)
    return True


def create_sample_data():
    """Create sample records if the CSV is empty."""

    df = load_ratings()

    if not df.empty:
        return

    sample = [
        [1, "Aarav", "Kesariya", "Arijit Singh",
         "Bollywood", "Favorites", 5],

        [2, "Riya", "Kesariya", "Arijit Singh",
         "Bollywood", "Favorites", 4],

        [3, "Meera", "Perfect", "Ed Sheeran",
         "Pop", "English Hits", 5],

        [4, "Kabir", "Perfect", "Ed Sheeran",
         "Pop", "English Hits", 4],

        [5, "Aarav", "Believer", "Imagine Dragons",
         "Rock", "Workout", 4],

        [6, "Riya", "Believer", "Imagine Dragons",
         "Rock", "Workout", 5],

        [7, "Meera", "Apna Bana Le", "Arijit Singh",
         "Bollywood", "Favorites", 5],

        [8, "Kabir", "Calm Down", "Rema",
         "Afrobeats", "Party", 4],

        [9, "Aarav", "Levitating", "Dua Lipa",
         "Pop", "Party", 3],

        [10, "Riya", "Apna Bana Le", "Arijit Singh",
         "Bollywood", "Favorites", 5]
    ]

    sample_df = pd.DataFrame(
        sample,
        columns=COLUMNS
    )

    sample_df.to_csv(
        DATA_FILE,
        index=False
    )