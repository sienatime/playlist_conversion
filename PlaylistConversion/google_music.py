from gmusicapi import Mobileclient
from music_library import MusicLibrary
import os

class GoogleMusic:
  def __init__(self):
    self.api = self.log_in()
    self.library = self.load_library()

  def log_in(self):
    email = os.environ['GOOGLE_ACCOUNT_EMAIL']
    password = os.environ['GOOGLE_ACCOUNT_ACCESS_TOKEN']
    api = Mobileclient()
    logged_in = api.login(email, password, Mobileclient.FROM_MAC_ADDRESS)
    # logged_in is True if login was successful
    if not logged_in:
      print "Sorry, those credentials weren't accepted."
      return
    return api

  def load_library(self):
    # Get all of the users songs.
    # library is a big list of dictionaries, each of which contains a single song.
    print 'Loading songs from Google...'
    gm_songs = self.api.get_all_songs()
    print 'done.'

    print 'Making library...'
    library = MusicLibrary(gm_songs)
    print 'done.'
    return library

  def make_playlist(self, name):
    playlist_id = self.api.create_playlist(name)
    print "Made playlist", name
    return playlist_id

  def delete_playlist(self, playlist_id):
    self.api.delete_playlist(playlist_id)

  def find_song(self, track):
    return self.library.find_song(track.artist, track.title)

  def add_to_playlist(self, playlist_id, song_ids):
    self.api.add_songs_to_playlist(playlist_id, song_ids)

  def logout(self):
    self.api.logout()
    print "Bye."
