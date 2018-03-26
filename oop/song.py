class Song:
    """ Class to represent a song
    
    Attributes:
        title (str): The title of the song
        artist (Artist): An artist object representing the songs creator
        duration (int): The duration of the song in seconds. May be zero """

    def __init__(self, title, artist, duration=0):

        self.title = title
        self.artist = artist
        self.duration = duration


class Album:

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):

        """ Adds a song to track list

        Args:
            song (Song): A song to add.
            postition (Optional[int]): If specified, the song will be added to that position
            in the track list - inserting it between other songs if necessary"""

        if position is None:
            self.tracks.append(song)

        else:
            self.tracks.insert(position, song)

