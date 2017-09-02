# -*- coding: utf-8 -*-
from playlist_parser import PlaylistParser
from playlist_parser import PlaylistTrack

def test_breakdown():
  ascii_parser = PlaylistParser("fixtures/ascii_playlist.m3u")
  assert(len(ascii_parser.tracks) == 2)

  manic_depression = ascii_parser.tracks[0]
  assert(manic_depression.artist == 'Jimi Hendrix')
  assert(manic_depression.title == 'Manic Depression')

  help_me_girl = ascii_parser.tracks[1]
  assert(help_me_girl.artist == 'Animals')
  assert(help_me_girl.title == 'Help Me, Girl')

  utf8_parser = PlaylistParser("fixtures/utf8_playlist.m3u8")
  assert(len(utf8_parser.tracks) == 1)
  katamari_taino = utf8_parser.tracks[0]
  assert(katamari_taino.artist == u"浅香　唯")
  assert(katamari_taino.title == u"カタマリたいの")

def test_song_with_dash():
  playlist_track = PlaylistTrack("A Band - A Thing - Another Thing")
  assert(playlist_track.artist == 'A Band')
  assert(playlist_track.title == 'A Thing - Another Thing')

def main():
  test_breakdown()
  test_song_with_dash()
  print "All tests passed"

if __name__ == "__main__":
  main()
