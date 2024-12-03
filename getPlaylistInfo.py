from spotipy import Spotify


def pick_a_playlist():
    PLAYLIST_LINK = str(input("Please input the link to the spotify playlist"))
    return PLAYLIST_LINK


def get_playlist_id(playlist_link):
    # return playlist id
    return playlist_link.split("/")[-1].split("?")[0]


def getting_playlist_information(playlist_id: str, SP: Spotify):
    # returns a json of all the information in the playlist
    playlistInfo = SP.user_playlist_tracks("luigi.puma",playlist_id)
    t = playlistInfo['items']
    while playlistInfo['next']:
        playlistInfo = SP.next(playlistInfo)
        t.extend(playlistInfo['items'])
    return t


def extracting_song_artist_uri(items, i):
    # returns a single song, artist and uri of the song
    song = items[i]['track']
    track_name = song['name']
    artist_name = song['artists'][0]['name']
    result = track_name.lower() #+ ' performed by ' + artist_name
    uri = song['uri']
    return [result, uri]


def getSongInfo(function_playlist):
    # returns a list of the songs with their artists and uri's
    # each element has the form ['song performed by artist', song uri]
    items = function_playlist
    songs = []
    for i in range(0, len(items)):
        songs.append(extracting_song_artist_uri(items, i))
    return songs


def getPlaylistInformation(SP: Spotify, PLAYLIST_LINK : str):
    playlistID = get_playlist_id(PLAYLIST_LINK)
    playlistData = getting_playlist_information(playlistID, SP)
    songs = getSongInfo(playlistData)
    return playlistID, songs
