import spotipy
from spotipy import SpotifyOAuth, CacheFileHandler

import hiddenVariables


def connect_to_spotify():
    CLIENT_ID = hiddenVariables.CLIENT_ID
    CLIENT_SECRET = hiddenVariables.CLIENT_SECRET
    SPOTIFY_REDIRECT_URI = hiddenVariables.SPOTIFY_REDIRECT_URI
    spotify_scope = hiddenVariables.spotify_scope
    SP = spotipy.Spotify(auth_manager=SpotifyOAuth(open_browser=False, scope=spotify_scope,
                                                   client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri=SPOTIFY_REDIRECT_URI,
                                                   cache_handler=CacheFileHandler(username='Luigi.puma')))

    return SP

