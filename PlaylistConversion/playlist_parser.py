# -*- coding: utf-8 -*-
import codecs

class PlaylistParser:
  def __init__(self, filename):
    self.tracks = self.load_playlist(filename)

  def load_playlist(self, filename):
    f = codecs.open(filename, encoding="utf-8")
    lines = f.readlines()
    tracks = []

    for line in lines:
      if line[0] == '#':
        tokens = line.split(',')
        if len(tokens) > 1:
          track_info =  ",".join(tokens[1:]).strip()
          track = PlaylistTrack(track_info)
          tracks.append(track)

    return tracks

class PlaylistTrack:
  def __init__(self, track_information):
    self.artist, self.title = self.parse_info(track_information)

  def parse_info(self, track_information):
    tokens = track_information.split(" - ")
    if len(tokens) >= 2:
      artist = tokens[0].strip()
      title = " - ".join(tokens[1:]).strip()
      return artist, title
