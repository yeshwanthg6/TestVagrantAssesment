# RecentPlaylistProgram
The RecentPlaylistProgram is an in-memory store that can accommodate N songs per user, with a fixed initial capacity.
It allows storing a list of song-user pairs, with each song linked to a user. 
The store keeps track of the recently played songs for each user and eliminates the least recently played songs when the store becomes full.

## Usage

To use RecentPlaylistProgram , follow the steps below:
1. Import necessary packages/classes:
'''
from collections import defaultdict, deque

class TestVargantUsersRecentPlayList:
'''

2. Create an instance of the TestVagrantUsersRecentPlayList class with the desired capacity:
'''
obj = TestVagrantUsersRecentPlayList(capacity=5)
'''

3. Add songs to the store for different users using the add_user_song method:
'''
obj.add_user_song("user1","s5")
obj.add_user_song("user1","s6")
obj.add_user_song("user2","s1")
obj.add_user_song("user2","s2")
'''

4. Retrieve the recently played songs for a specific user using the get_all_recently_played_songs method:
'''
print(obj.get_all_recently_played_songs("user1"))
print(obj.get_all_recently_played_songs("user2"))
'''

5. Retrieve the recently played songs for all user with help of special methos:
'''
print(repr(obj))
'''

EXAMPLE:
Going through documentation takes time , so feel free to understand code here more comfortably:
store = TestVagrantUsersRecentPlayList(capacity=5)

store.add_user_song("user1","s1")

store.add_user_song("user1","s2")

store.add_user_song("user1","s3")

store.add_user_song("user1","s4")

store.add_user_song("user1","s5")

store.add_user_song("user1","s6")

print(store.get_all_recently_played_songs("user1")) #Output :['s2', 's3', 's4', 's5', 's6']

store.add_user_song("user2","s1")

store.add_user_song("user2","s2")

store.add_user_song("user2","s3")

store.add_user_song("user2","s4")

print(store.get_all_recently_played_songs("user2")) #Output :['s1', 's2', 's3', 's4']

print(repr(store)) #Output : RecentlyPlayedStore(capacity=5, store={'user1': deque(['s2', 's3', 's4', 's5', 's6']), 'user2': deque(['s1', 's2', 's3', 's4'])})


----------------------------------------------------Thanks, Hope Document helps----------------------------------------------------
