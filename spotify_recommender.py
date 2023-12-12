favorite_artists=['confetti', 'nf', 'bakermat', 'stellar']

# client_id = ADD YOUR SPOTIFY ID
# client_secret = ADD YOUR SPOTIFY KEY
redirect_uri='https://localhost'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret))
redirect_uri='https://localhost'

## -------- Code below --------- ##

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials



spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret))

# get a list of favorite artists and their identifiers
favorite_artist_uris = []

for artist in favorite_artists:
    res = spotify.search(artist, type='artist', market='US', limit=1, offset=0)
    favorite_artist_uris.append(res['artists']['items'][0]['uri'])

def get_song(response):
    return {
        'name': response['name'],
        'artists': [artist['name'] for artist in response['artists']], 
        'album': response['album']['name'],
        'preview_url': response['preview_url'],
        'uri': response['uri'],
    }

def get_recs(filters: dict, current_songs: set):
    # This gets all the local vars in a dictionary format
    try: 
        res = spotify.recommendations(seed_artists=favorite_artist_uris, limit=10, country='US', **filters)
        for track in res['tracks']:
            song = get_song(track)
            if song['uri'] not in current_songs:
                return song
        print("No new song found")
        return None
    except IndexError as e: 
        print("No song found", filters)
        return None
        
