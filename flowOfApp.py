import spotifyConnection
import getPlaylistInfo
import duplicateFinding
import deleteSongs


def duplicateSongs():
    SP = spotifyConnection.connect_to_spotify()
    playlistID, songs = getPlaylistInfo.getPlaylistInfomation(SP)
    duplicates = duplicateFinding.findDuplicates(songs)
    if duplicates:
        deleteSongs.duplicateDeletion(duplicates, playlistID, SP)