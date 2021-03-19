import pathlib
import pandas as pd

pathlib.Path('output').mkdir(exist_ok=True)

df = pd.read_csv('./spotify.csv')

print(df.columns)
df = df.sort_values(by=['track_popularity'], ascending=False)
df_noDuplicates = df.drop_duplicates('track_name')

df_noDuplicates.drop("track_id", inplace=True, axis=1)
df_noDuplicates.drop("track_album_id", inplace=True, axis=1)
df_noDuplicates.drop("playlist_name", inplace=True, axis=1)
df_noDuplicates.drop("playlist_id", inplace=True, axis=1)
df_noDuplicates.drop("playlist_subgenre", inplace=True, axis=1)
df_noDuplicates.drop("mode", inplace=True, axis=1)


df_noDuplicates.to_csv('./output/new_spotify.csv', index=False)