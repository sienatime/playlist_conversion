# About This Project

This project uses the [gmusicapi](https://github.com/simon-weber/gmusicapi) Python library to convert m3u or m3u8 playlists into Google Play Music playlists.

# Setup

Install dependencies (virtualenv recommended: `pip install -r requirements.txt`) and set the required environment variables:

* `GOOGLE_ACCOUNT_EMAIL`: the email address of the Google account for which you would like to create playlists
* `GOOGLE_ACCOUNT_PASSWORD`: the password (or app-specific password) for the Google account. If you use two-factor authentication (*strongly recommended*), you will need to create an app-specific password. Read more about that [here](https://support.google.com/accounts/answer/185833?hl=en).

# Sample Usage

From a file named `file_name.m3u`, create a new playlist on Google Play Music called "New Playlist" and add all the songs.

```
from PlaylistConversion.convert_playlist import PlaylistConverter
pc = PlaylistConverter()
pc.convert_playlist("New Playlist", "file_name.m3u")
pc.done()
```
