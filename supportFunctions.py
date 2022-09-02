import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import hiddenVariables
import math


def connect_to_spotify():
    CLIENT_ID = hiddenVariables.CLIENT_ID
    CLIENT_SECRET = hiddenVariables.CLIENT_SECRET

    CLIENT_CREDENTIALS_MANAGER = SpotifyClientCredentials(
        client_id=CLIENT_ID, client_secret=CLIENT_SECRET
    )
    SP = spotipy.Spotify(client_credentials_manager=CLIENT_CREDENTIALS_MANAGER)
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
    playlist_uri = get_playlist_uri(PLAYLIST_LINK)
    for track in SP.playlist_tracks(playlist_uri)["items"]:
        track_name = track["track"]["name"]
        artist_name = track["track"]["artists"][0]["name"]
        result = track_name + ' performed by ' + artist_name
        songs.append(result)

    return songs


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
                print("{0}, \tnumber of repeats in the playlist: {1} ".format(duplicates[i], no_of_duplicates[i]))
    else:
        print("There are no duplicates")


def checkPlaylistForDuplicate_songs():
    #    PLAYLIST_LINK = pick_a_playlist()
    PLAYLIST_LINK = "https://open.spotify.com/playlist/6zDGeRmorl0imFVn82U04f?si=35873ee5dc39423f"
    SP = connect_to_spotify()
    songs = get_songs_with_artist(PLAYLIST_LINK, SP)
    duplicates, no_of_duplicates = findDuplicates(songs)
    no_of_duplicates = get_correct_no_of_duplicates(no_of_duplicates)
    showDuplicates(duplicates, no_of_duplicates)


checkPlaylistForDuplicate_songs()
