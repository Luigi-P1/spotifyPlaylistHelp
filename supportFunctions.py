import spotipy
from spotipy import CacheFileHandler
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import hiddenVariables
import math


def connect_to_spotify():
    CLIENT_ID = hiddenVariables.CLIENT_ID
    CLIENT_SECRET = hiddenVariables.CLIENT_SECRET
    SPOTIFY_REDIRECT_URI = hiddenVariables.SPOTIFY_REDIRECT_URI
    spotify_scope = hiddenVariables.spotify_scope
    CLIENT_CREDENTIALS_MANAGER = SpotifyClientCredentials(
        client_id=CLIENT_ID, client_secret=CLIENT_SECRET
    )
    SP = spotipy.Spotify(auth_manager=SpotifyOAuth(open_browser=False, scope=spotify_scope,
                                                   client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET,
                                                   redirect_uri=SPOTIFY_REDIRECT_URI,
                                                   cache_handler=CacheFileHandler(username='Luigi.puma')))

    return SP


def pick_a_playlist():
    PLAYLIST_LINK = str(input("Please input the link to the spotify playlist"))
    return PLAYLIST_LINK


def get_playlist_uri(playlist_link):
    # return playlist id
    return playlist_link.split("/")[-1].split("?")[0]


def get_songs_with_artist(PLAYLIST_LINK, SP):
    # returns a list of songs in the playlist with the artists
    songs = []
    song_uri = []
    playlist_id = get_playlist_uri(PLAYLIST_LINK)
    function_playlist = SP.playlist(playlist_id)
    items = function_playlist['tracks']['items']
    for i in range(0, len(items)):
        song = items[i]['track']
        track_name = song['name']
        artist_name = song['artists'][0]['name']
        result = track_name + ' performed by ' + artist_name
        songs.append(result)
        song_uri.append(song['uri'])
    return songs, song_uri


def findDuplicates(textList: list):
    duplicates = []
    no_of_duplicates = []
    for i in range(0, len(textList)):
        for j in range(i + 1, len(textList)):
            if textList[i] == textList[j]:
                if textList[i] not in duplicates:
                    duplicates.append(textList[i])
                    no_of_duplicates.append(1)
                else:
                    location = duplicates.index(textList[i])
                    no_of_duplicates[location] += 1
    return duplicates, no_of_duplicates


def get_correct_no_of_duplicates(no_of_duplicates: list):
    for i in range(0, len(no_of_duplicates)):
        result = math.sqrt((8 * no_of_duplicates[i] + 1) / 4) - 0.5
        no_of_duplicates[i] = int(result)
    return no_of_duplicates


def showDuplicates(duplicates: list, no_of_duplicates: list):
    total_no_of_duplicates = sum(no_of_duplicates)
    if len(duplicates) != 0:
        if total_no_of_duplicates == 1:
            print("There is 1 duplicate song in this playlist:\n{0} number of repeats in the playlist: {1}".
                  format(duplicates[0], no_of_duplicates[0]))
        else:
            print("There are {0} duplicate songs in this playlist:".format(len(duplicates)))
            for i in range(0, len(duplicates)):
                print("{0},".format(duplicates[i]).ljust(60) + "Number of repeats in the playlist: {0} "
                      .format(no_of_duplicates[i]))
    else:
        print("There are no duplicate songs in the playlist.")


def deleteDuplicatesOption():
    print("If you would like to delete the duplicates then type Y or y.")
    response = str(input())
    if response in ["Y", "y"]:
        return True
    else:
        return False


def getIndicesOfDuplicates(songs: list, duplicates: list):
    duplicateIndices = []
    for i in duplicates:
        indices = [j for j, x in enumerate(songs) if x == i]
        indices.remove(indices[0])
        for j in indices:
            duplicateIndices.append(j)
    return duplicateIndices


def getDuplicatesUri(duplicateIndices: list, song_uri: list):
    duplicateUri = []
    for i in duplicateIndices:
        uri = song_uri[i]
        duplicateUri.append(uri)
    return duplicateUri


def deleteDuplicates(duplicateUri: list, PLAYLIST_LINK: str, SP: spotipy):
    SP.playlist_remove_all_occurrences_of_items(playlist_id=PLAYLIST_LINK, items=duplicateUri)


def deleteDuplicatesFromPlaylist(songs: list, duplicates: list, song_uri: list, PLAYLIST_LINK: str, SP: spotipy):
    duplicateIndices = getIndicesOfDuplicates(songs, duplicates)
    duplicateUri = getDuplicatesUri(duplicateIndices, song_uri)
    deleteDuplicates(duplicateUri, PLAYLIST_LINK, SP)


def checkPlaylistForDuplicate_songs():
    #   PLAYLIST_LINK = pick_a_playlist()
    PLAYLIST_LINK = "https://open.spotify.com/playlist/6zDGeRmorl0imFVn82U04f?si=35873ee5dc39423f"
    SP = connect_to_spotify()
    songs, song_uri = get_songs_with_artist(PLAYLIST_LINK, SP)
    duplicates, no_of_duplicates = findDuplicates(songs)
    no_of_duplicates = get_correct_no_of_duplicates(no_of_duplicates)
    showDuplicates(duplicates, no_of_duplicates)
    if len(duplicates) != 0:
        choice = deleteDuplicatesOption()
        if choice:
            deleteDuplicatesFromPlaylist(songs, duplicates, song_uri, PLAYLIST_LINK, SP)


checkPlaylistForDuplicate_songs()
