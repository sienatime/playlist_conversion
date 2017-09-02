from PlaylistConversion.google_music import GoogleMusic
from PlaylistConversion.playlist_parser import PlaylistParser

class PlaylistConverter:
  def __init__(self):
    self.service = GoogleMusic()

  def done(self):
    self.service.logout()

  def convert_playlist(self, playlist_name, filename):
    playlist_id = self.service.make_playlist(playlist_name)

    try:
      parser = PlaylistParser(filename)
      song_ids = []

      for i in xrange(len(parser.tracks)):
        track = parser.tracks[i]
        song = self.service.find_song(track)
        if song:
          song_ids.append(song.id)
        else:
          print "couldn't find song at track #", i + 1, track.artist, track.title

      self.service.add_to_playlist(playlist_id, song_ids)
    except:
      self.service.delete_playlist(playlist_id)
      raise
