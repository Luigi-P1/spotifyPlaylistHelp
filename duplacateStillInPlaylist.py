from spotipy import Spotify

import getPlaylistInfo


def getSondTitles(SP: Spotify, PLAYLIST_LINK: str):
    items =  getPlaylistInfo.getPlaylistInformation(SP, PLAYLIST_LINK)[1]
    songTitles = []
    for item in items:
        songTitles.extend([item[0]])
    return songTitles


def checkDuplecateStillInPlay(playlistSongTitles: list, duplecates: list, SP: Spotify, playlistID):
    stillIn = []
    for duplecate in duplecates:
        #print(duplecate[0])
        #print(playlistSongTitles)
        if duplecate[0] not in playlistSongTitles:
            if duplecate[0] not in stillIn:
                SP.playlist_add_items(playlist_id=playlistID, items=[duplecate[1]])
                stillIn.extend([duplecate[0]])
                #print(duplecate)
#                print(stillIn)


def duplecateStillExists(SP: Spotify, PLAYLIST_LINK: str, duplecates: list, playlistID):
    playlistSongTitles = getSondTitles(SP, PLAYLIST_LINK)
    checkDuplecateStillInPlay(playlistSongTitles, duplecates, SP, playlistID)