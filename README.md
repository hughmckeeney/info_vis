# info_vis

Contains original spotify data, a script to clean it and the cleaned spotify data. The original dataset can be found here: https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv 
with details here: https://github.com/rfordatascience/tidytuesday/blob/master/data/2020/2020-01-21/readme.md

The cleaned spotify data does not contain any duplicate song names. The song duplicates were removed, keeping the most popular entry for each song. 

The following features were also removed as they were not relevant for this assignment:
"track_id"
"track_album_id"
"playlist_name"
"playlist_id"
"playlist_subgenre"
"mode"

The dataset was sorted by "track_popularity" in descending order
