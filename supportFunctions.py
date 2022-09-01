from os.path import exists

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import hiddenVariables

CLIENT_ID = hiddenVariables.CLIENT_ID
CLIENT_SECRET = hiddenVariables.CLIENT_SECRET
PLAYLIST_LINK = "https://open.spotify.com/playlist/6zDGeRmorl0imFVn82U04f?si=35873ee5dc39423f"

CLIENT_CREDENTIALS_MANAGER = SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET
)
SP = spotipy.Spotify(client_credentials_manager=CLIENT_CREDENTIALS_MANAGER)


def get_playlist_uri(playlist_link):
    # return playlist id
    return playlist_link.split("/")[-1].split("?")[0]


def get_songs_with_artist():
    # returns a list of songs in the playlist with the artists
    songs = []
    playlist_uri = get_playlist_uri(PLAYLIST_LINK)
    for song in SP.playlist_tracks(playlist_uri)["items"]:
        track_name = song["song"]["name"]
        artist_name = song["song"]["artists"][0]["name"]
        result = track_name + ' performed by ' + artist_name
        songs.append(result)

    return songs


def findDuplicates(textList: list):
    duplicates = []
    for i in range(0, len(textList)):
        for j in range(i + 1, len(textList)):
            if textList[i] == textList[j] and textList[i] not in duplicates:
                duplicates.append(textList[i])
    return duplicates


def showDuplicates(duplicates: list):
    noOfDuplicates = len(duplicates)
    if len(duplicates) != 0:
        if noOfDuplicates == 1:
            print("There is 1 duplicate song in this playlist:\n{0}".format(duplicates[0]))
        else:
            print("There are {0} duplicate songs in this playlist:".format(len(duplicates)))
            for i in duplicates:
                print(i)
    else:
        print("There are no duplicates")


def checkPlaylistForDuplicate_songs():
    songs = get_songs_with_artist()
    duplicates = findDuplicates(songs)
    showDuplicates(duplicates)


checkPlaylistForDuplicate_songs()
