'''
TODO:
- config file for auth
- comments
- proper readme file
'''



'''
before running the python file:

export your spotify client id and secret as
    export SPOTIPY_CLIENT_ID='your id'
    export SPOTIPY_CLIENT_SECRET='your secret'
'''


import sys
import spotipy
from ytmusicapi import YTMusic
from spotipy.oauth2 import SpotifyClientCredentials


ytmusic = YTMusic('headers/headers_auth.json')
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# playlistId = ytmusic.create_playlist('Winter of Love', 'from spotify')

# function to add track to the playlist
def add_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        num = 0
        track_details = '{} {}'.format(track['artists'][0]['name'], track['name']) 
        search_results = ytmusic.search(track_details)
        result = search_results[num]

        while result['resultType'] != 'song':
            num += 1
            result = search_results[num]

        ytmusic.add_playlist_items(playlistId, [result['videoId']])
        print('TRACK ADDED => {}  {}'.format(i, track_details))
        

username = 'spotify'

playlists = spotify.user_playlists(username)

while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
        if playlist['name'] == 'Winter of Love':
        # if playlist['owner']['id'] == username:
        #     if playlist['name'] == 'make_':
            print("Playlist ===> {} {}".format(i, playlist['name']))
            print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
            print('\n\n')

            results = spotify.user_playlist(username, playlist['id'], fields="tracks,next")
            tracks = results['tracks']
            add_tracks(tracks)
            while tracks['next']:
                tracks = spotify.next(tracks)
                add_tracks(tracks)

    if playlists['next']:
        playlists = spotify.next(playlists)
    else:
        playlists = None