def findDuplicates(Songs: list):
    duplicates = []
    for i in range(0, len(Songs)):
        for j in range(i + 1, len(Songs)):
            if Songs[i][0] == Songs[j][0]:
                if Songs[i] not in duplicates:
                    duplicates.append(Songs[i])
                if Songs[j] not in duplicates:
                    duplicates.append(Songs[j])
    return duplicates


def numberOfDuplicateInPlaylist(songs: list, duplicateTitle: str):
    noOfDuplicate = 0
    for song in songs:
        songTitle = song[0]
        if songTitle == duplicateTitle:
            noOfDuplicate += 1
    return noOfDuplicate


def findNumberOfEachDuplicate(duplicates: list, songs: list):
    numberOfEachDuplicate = []
    for i in duplicates:
        duplicateTitle = i[0]
        numberOfEachDuplicate.append(numberOfDuplicateInPlaylist(songs, duplicateTitle))
    return numberOfEachDuplicate


def showDuplicates(duplicates: list, no_of_duplicates: list):
    total_no_of_duplicates = sum(no_of_duplicates)
    if total_no_of_duplicates == 1:
        print("There is 1 duplicate song in this playlist:\n{0} number of repeats in the playlist: {1}".
              format(duplicates[0], no_of_duplicates[0]))
    elif total_no_of_duplicates >= 2:
        print("There are {0} duplicate songs in this playlist:".format(len(duplicates)))
        for i in range(0, len(duplicates)):
            print("{0},".format(duplicates[i]).ljust(60) + "Number of repeats in the playlist: {0} "
                  .format(no_of_duplicates[i]))
    else:
        print("There are no duplicate songs in the playlist.")


def findDuplicates(Songs: list):
    duplicates = findDuplicates(Songs)
    numberOfEachDuplicate = findNumberOfEachDuplicate(duplicates, Songs)
    showDuplicates(duplicates, numberOfEachDuplicate)
    return duplicates
