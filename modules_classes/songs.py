class song(object):
    
    def __init__(self, lyrics, instrument):
        self.lyrics = lyrics
        self.instrument = instrument


    def sing_me_a_song(self):
        print(self.instrument)
        for line in self.lyrics:
            print(line)
    
happy_bday = song(["Happy birthday to you",
                    "I dont want to get sued",
                    "So i'll stop right there"],
                    "guitar")

# rock_lyrics = ["I tried so far",
#                 "and got so far",],
#                 "drums"

# linkin_park = song(rock_lyrics)

bulls_on_parade = song(["they rally around the family",
                        "With pockets full of shells"],
                        "drums")

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
# linkin_park.sing_me_a_song()