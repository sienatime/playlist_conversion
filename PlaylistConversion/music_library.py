# sample data from google play music library (abbreviated):
# {
#    'id':'5924d75a-931c-30ed-8790-f7fce8943c85',
#    'nid':'Txsffypukmmeg3iwl3w5a5s3vzy',
#    'artistId':[
#      'Aod62yyj3u3xsjtooghh2glwsdi'
#    ],
#    'title':'Haxprocess',
#    'artist':'Opeth',
#  }

class MusicLibrary:
  def __init__(self, gm_songs):
    self.artists, self.songs = self.make_library(gm_songs)

  def make_library(self, gm_songs):
    artists = {} # key: artist name, value: list of Song
    songs = {}
    for gm_song in gm_songs:
      artist_name = gm_song['artist']
      if not artists.get(artist_name):
        artist = Artist(artist_name)
        song = Song(gm_song['id'], gm_song['title'])
        artist.add_song(song)
        artists[artist_name] = artist
      else:
        artist = artists[artist_name]
        song = Song(gm_song['id'], gm_song['title'])
        artist.add_song(song)
      songs[song.title] = song

    return artists, songs

  def find_song(self, artist_name, song_title):
    artist = self.artists.get(artist_name)
    if artist and artist.get_song(song_title):
      return artist.get_song(song_title)
    else:
      return self.songs.get(song_title)

class Artist:
  def __init__(self, name):
    self.name = name
    self.songs = {}

  def add_song(self, song):
    if not self.songs.get(song.title):
      self.songs[song.title] = song

  def get_song(self, title):
    return self.songs.get(title)

class Song:
  def __init__(self, id, title):
    self.id = id
    self.title = title
