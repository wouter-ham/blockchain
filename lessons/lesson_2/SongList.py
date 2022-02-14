class SongNode:
    def __init__(self, song_title: str | None = None, next=None, previous=None):
        self.song_title: str = song_title
        self.next: SongNode = next
        self.previous: SongNode = previous


class SongList:
    def __init__(self):
        self.head: SongNode | None = None

    def printSongs(self) -> None:
        current: SongNode = self.head
        while current is not None:
            print(current.song_title)
            current = current.next

    def AddNewSong(self, new_song_title: str) -> None:
        tail: SongNode = self.getTail()
        new_node: SongNode = SongNode(new_song_title, previous=tail)
        tail.next = new_node

    def getTail(self) -> SongNode:
        current: SongNode = self.head
        if current.next is None:
            return current
        while current.next is not None:
            current = current.next
        return current

    def printAll(self):
        current: SongNode = self.head
        while current is not None:
            print(
                (current.previous.song_title if current.previous is not None else '') +
                (' <- ' + current.song_title + ' -> ') +
                (current.next.song_title if current.next is not None else '')
            )
            current = current.next
