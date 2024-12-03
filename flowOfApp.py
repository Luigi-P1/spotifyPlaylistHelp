import spotifyConnection
import getPlaylistInfo
import duplicateFinding
import deleteSongs
import duplacateStillInPlaylist

def duplicateSongs():
    SP = spotifyConnection.connect_to_spotify()
    playlistLink = getPlaylistInfo.pick_a_playlist()
    playlistID, songs = getPlaylistInfo.getPlaylistInformation(SP, playlistLink)
    duplicates = duplicateFinding.findDuplicates(songs)
    if duplicates:
        deleteSongs.duplicateDeletion(duplicates, playlistID, SP)
        duplacateStillInPlaylist.duplecateStillExists(SP, playlistLink, duplicates, playlistID)