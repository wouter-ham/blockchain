class SongNode:
    def __init__(self, song_title: str | None = None, next=None):
        self.song_title: str = song_title
        self.next: SongNode = next


class SongList:
    def __init__(self):
        self.head: SongNode | None = None

    def printSongs(self) -> None:
        current: SongNode = self.head
        while current is not None:
            print(current.song_title)
            current = current.next

    def AddNewSong(self, new_song_title: str) -> None:
        self.getTail().next = SongNode(new_song_title)

    def getTail(self) -> SongNode:
        current: SongNode = self.head
        if current.next is None:
            return current
        while current.next is not None:
            current = current.next
        return current
