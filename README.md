# Sample Usage

From a file named `file_name.m3u`, create a new playlist on Google Play Music called "New Playlist" and add all the songs.

```
from convert_playlist import PlaylistConverter
pc = PlaylistConverter()
pc.convert_playlist("New Playlist", "file_name.m3u")
pc.done()
```
