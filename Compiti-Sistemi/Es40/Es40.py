class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        # lyrics is a list of lines
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
print("*"*10)
bulls_on_parade.sing_me_a_song()

# Study Drills 1-2
hotel_california_lyrics = ["Welcome to the Hotel California",
                    "Such a lovely place (Such a lovely place)",
                    "Such a lovely face",
                    "Plenty of room at the Hotel California",
                    "Any time of year (Any time of year)",
                    "You can find it here"]

paradise_city_lyrics = ["Take me down to the Paradise City",
                        "Where the grass is green and the girls are pretty",
                        "Oh, won't you please take me home? Yeah-yeah",
                        "Take me down to the Paradise City",
                        "Where the grass is green and the girls are pretty",
                        "Take me home"]

africa_lyrics = ["It's gonna take a lot to drag me away from you",
                 "There's nothing that a hundred men or more could ever do",
                 "I bless the rains down in Africa",
                 "Gonna take some time to do the things we never had"]

hotel_california_song = Song(hotel_california_lyrics)
paradise_city_song = Song(paradise_city_lyrics)
africa_song = Song(africa_lyrics)

print("*"*10)
hotel_california_song.sing_me_a_song()
print("*"*10)
paradise_city_song.sing_me_a_song()
print("*"*10)
africa_song.sing_me_a_song()

#   Study Drills
#   1. Write some more songs using this and make sure you understand that you’re passing a list of
#   strings as the lyrics.
#   2. Put the lyrics in a separate variable, then pass that variable to the class to use instead.
#   3. See if you can hack on this and make it do more things. Don’t worry if you have no idea how, just
#   give it a try, see what happens. Break it, trash it, thrash it, you can’t hurt it.
#   4. Search online for ”object-oriented programming” and try to overflow your brain with what you
#   read. Don’t worry if it makes absolutely no sense to you. Half of that stuff makes no sense to me
#   too.
