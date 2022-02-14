
class SongNode:
    def __init__(self, song_title=None, next = None):
        self.song_title = song_title
        self.next = next

class SongList:
    def __init__(self):  
        self.head = None

    def printSongs(self): 
        print("Nothing is printed")

    def AddNewSong(self, new_song_title):
        pass