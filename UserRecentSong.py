from collections import defaultdict, deque


class TestVagrantUsersRecentPlayList:
    def __init__(self, capacity):
        """
        Constructor
        deque - double ended queue
        """
        self.capacity = capacity
        self.store_song = defaultdict(deque)

    def add_user_song(self, user, song):
        """
        Method checks if a user's recent playlist exceeds assigned capacity ,Pops a value from left
        """
        if len(self.store_song[user]) == self.capacity:
            self.store_song[user].popleft()
        self.store_song[user].append(song)

    def get_all_recently_played_songs(self, user):
        """
        returns list of songs played by user
        """
        return list(self.store_song[user])

    def __repr__(self):
        """
        returns complete information of user and songs related to an object
        ex: print(repr(obj))
        """
        return f"RecentlyPlayedStore(capacity={self.capacity}, store={dict(self.store_song)})"




