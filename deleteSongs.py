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
    SP.playlist_remove_all_occurrences_of_items(playlist_id=PLAYLIST_LINK, items=songsUri)


def duplicateDeletion(duplicates: list, PLAYLIST_LINK: str, SP: spotipy):
    option = deleteDuplicatesOption()
    if option:
        duplicateUris = getDuplicateUris(duplicates)
        deleteDuplicates(duplicateUris, PLAYLIST_LINK, SP)