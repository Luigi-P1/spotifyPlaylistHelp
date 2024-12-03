from math import floor

import spotipy


def getDuplicateUris(duplicates: list):
    duplicateUris = []
    for duplicate in duplicates:
        duplicateUris.append(duplicate[1])
    return duplicateUris


def deleteDuplicatesOption():
    print("If you would like to delete the duplicates then type Y or y.")
    response = str(input())
    if response in ["Y", "y"]:
        return True
    else:
        return False


def deleteDuplicates(songsUri: list, PLAYLIST_LINK: str, SP: spotipy):
    timesDeleteIsUsed = floor(len(songsUri)/50)
    if timesDeleteIsUsed >0:
        for i in range(1,timesDeleteIsUsed+1) :
            songs = songsUri[(i-1)*50:i*50]
            SP.playlist_remove_all_occurrences_of_items(playlist_id=PLAYLIST_LINK, items=songs)
    songs = songsUri[timesDeleteIsUsed * 50:len(songsUri)]
    SP.playlist_remove_all_occurrences_of_items(playlist_id=PLAYLIST_LINK, items=songs)


def duplicateDeletion(duplicates: list, PLAYLIST_LINK: str, SP: spotipy):
    option = deleteDuplicatesOption()
    if option:
        duplicateUris = getDuplicateUris(duplicates)
        deleteDuplicates(duplicateUris, PLAYLIST_LINK, SP)
