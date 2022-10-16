# spotifyPlaylistHelp
### purpose:
In spotify if someone trys to add a song that is already in the playlist there are two possibilities:

- If the song is in the same album there will be a pop-up warning that the song is already in the playlist.
- However, if a song is in a different album by the same artist spotify wouldn't detect this.

The latter of these cases is what this project attempts to rectify; 
through checking if multiple iterations of a song appear in a playlist 
only looking at the song title and the artist and giving the option to 
automatically delete these duplicates.

###How to use
go into the hiddenVariable.py and add the relevant values for the following variables:

- CLIENT_ID = ' '
- CLIENT_SECRET = ' '
- SPOTIFY_REDIRECT_URI = ' '
- USER_NAME = ' '

For the first three variables visit the following link:

For the last one use your personal spotify username