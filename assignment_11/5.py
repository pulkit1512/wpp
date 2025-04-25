import pandas as pd
import itertools

# Example concert data
concerts = pd.DataFrame({
    "artist": ["A", "B", "C", "A", "B"],
    "venue": ["X", "Y", "Z", "X", "Y"],
    "date": ["2023-01", "2023-01", "2023-02", "2023-02", "2023-03"]
})

# Generate all artist-venue pairs
artists = pd.Series(["A", "B", "C"])
venues = pd.Series(["X", "Y", "Z"])
pairs = list(itertools.product(artists, venues))

# Create wide table
concert_counts = concerts.groupby(["date", "artist", "venue"]).size().unstack(fill_value=0)
print("Concert Counts (Wide Table):\n", concert_counts)
