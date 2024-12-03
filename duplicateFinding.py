def again(Songs, i, duplicates):
    for j in range(i + 1, len(Songs)):
        if Songs[i][0] == Songs[j][0]:
            if Songs[j] not in duplicates:
                duplicates.append(Songs[j])
    return duplicates


def findDuplicate(Songs: list):
    duplicates = []
    for i in range(0, len(Songs)):
        duplicates = again(Songs, i, duplicates)
    return duplicates


def numberOfDuplicateInPlaylist(songs: list, duplicateTitle: str):
    noOfDuplicate = -1
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
    total_no_of_duplicates = 0
    whatToSay = ""
    if len(duplicates) == 1:
        print("There is 1 duplicate song in this playlist:\n{0} number of repeats in the playlist: {1}".
              format(duplicates[0], no_of_duplicates[0]))
    elif len(duplicates) >= 2:
        for i in range(0, len(duplicates)):
            if no_of_duplicates[i] > 1 and duplicates[i][0] == duplicates[i-1][0]:
                continue
            whatToSay +=("{0},".format(duplicates[i][0]).ljust(60) + "Number of repeats in the playlist: {0} \n"
                  .format(no_of_duplicates[i]))
            total_no_of_duplicates += no_of_duplicates[i]
        print("There are {0} duplicate songs in this playlist:".format(total_no_of_duplicates))
        print(whatToSay)
    else:
        print("There are no duplicate songs in the playlist.")


def findDuplicates(Songs: list):
    duplicates = findDuplicate(Songs)
    numberOfEachDuplicate = findNumberOfEachDuplicate(duplicates, Songs)
    showDuplicates(duplicates, numberOfEachDuplicate)
    return duplicates
