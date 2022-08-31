from os.path import exists

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import hiddenVariables

CLIENT_ID = hiddenVariables.CLIENT_ID
CLIENT_SECRET = hiddenVariables.CLIENT_SECRET
PLAYLIST_LINK = "https://open.spotify.com/playlist/5Ug6At5op0DSnoLXaw7a1W?si=fc6b3783f1db48c8"

CLIENT_CREDENTIALS_MANAGER = SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET
)
SP = spotipy.Spotify(client_credentials_manager=CLIENT_CREDENTIALS_MANAGER)


def get_playlist_uri(playlist_link):
    # return playlist id
    return playlist_link.split("/")[-1].split("?")[0]


def get_tracks():
    # returns a list of songs in the playlist
    tracks = []
    playlist_uri = get_playlist_uri(PLAYLIST_LINK)
    for track in SP.playlist_tracks(playlist_uri)["items"]:
        track_name = track["track"]["name"]
        result = track_name
        tracks.append(result)

    return tracks


def getPathOfText():
    print("Which text file do you want to check?")
    filePath = input()
    file_exists = exists(filePath)
    while not file_exists:
        filePath = input("Error!! path doesn't exist please input the right file.")
        file_exists = exists(filePath)
    return filePath


def readTextFile(file_name):
    f = open(file_name, encoding="utf8")
    file_content = f.readlines()
    f.close()
    return file_content


def findDuplicates(textList: list):
    duplicates = []
    for i in range(0, len(textList)):
        for j in range(i + 1, len(textList)):
            if textList[i] == textList[j] and textList[i] not in duplicates:
                duplicates.append(textList[i])
    return duplicates


def showDuplicates(duplicates: list):
    if len(duplicates) != 0:
        print("There are {0} duplicate songs in this playlist:".format(len(duplicates)))
        for i in duplicates:
            print(i)
    else:
        print("There are no duplicates")


def checkPlaylistForDuplicates():
    fileName = getPathOfText()
    text = readTextFile(fileName)
    duplicates = findDuplicates(text)
    showDuplicates(duplicates)

print(get_tracks())