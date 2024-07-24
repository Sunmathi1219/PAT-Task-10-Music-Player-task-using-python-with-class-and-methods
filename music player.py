"""
create a music player class using python  with the following features-1.users can create audio using URLs available online.
2.users can create multiple playlists based on the genre of the song.3.users can add multiple audio files into each playlist created. 
4.users can search audio by name 5.users can search the playlist by name 5.users can give ratings to playlist and audio.
rating displayed is the average rating calculated after each submission.6.for displaying average rating-create 3 users and randomly 
generate ratings from 1 to 5,find the average rating from the random number generated.6.audio player customization will fetch 
additional points using python class and methods
"""

import random

#create audio using URL's
class Audio:

    def __init__(self,url,name):

        self.url=url
        self.name=name
        self.ratings=[]

    #add rating to playlist
    def add_ratings(self,rating):
        if 1<=rating<=5:
            self.ratings.append(rating)    
    
        else:
            print("Ratings Should be with the range of 1 to 5")

    #calculate average rating
    @property
    def average_rating(self):
        if self.ratings:
            return sum(self.ratings)/len(self.ratings)

        else:
            return 0  

    def __str__(self):
        return f"Audio(name={self.name},url={self.url},average_rating={self.average_rating:.2f})"          


class Playlist:
    def __init__(self,name,genre):
        self.name=name
        self.genre=genre
        #users can add audio file
        self.audios=[]
        self.ratings=[]
    
    #users can add audio file 
    def add_audio(self,audio):
        self.audios.append(audio)

    #user can search audio by name
    def search_audio_by_name(self,name):
        return [audio for audio in self.audios if audio.name.lower()==name.lower()]
    
    # add ratings to playlist
    def add_ratings(self,rating):
        if 1<=rating<=5:
            self.ratings.append(rating)    
    
        else:
            print("Ratings Should be with the range of 1 to 5")

   #calculate average rating
    @property
    def average_rating(self):
        if self.ratings:
            return sum(self.ratings)/len(self.ratings)

        else:
            return 0        
        
    def __str__(self):
        return f"playlist(name={self.name},genre={self.genre},average_rating={self.average_rating:.2f})"

#music player class
class MusicPlayer:
    def __init__(self):
        self.playlists=[]

    #create playlist
    def create_playlist(self,name,genre):
         self.playlists.append(Playlist(name,genre))
        
    #add audio files to playlist
    def add_audio_to_playlist(self,playlist_name,audio):
        for playlist in self.playlists:
            if playlist.name.lower() == playlist_name.lower():
                playlist.add_audio(audio)
                break

            else:
                print(f"No playlist is found with the name {playlist_name}")

    #search playlist by the name
    def search_playlist_by_name(self,name):
        return [playlist for playlist in self.playlists if playlist.name.lower()==name.lower()]

    def __str__(self):
        return '\n'.join(str(playlist) for playlist in self.playlists)


player= MusicPlayer()
player.create_playlist("Melody songs","Melody")
player.create_playlist("Hip pop songs","Hippop")

audio_1=Audio("chill beats","http://masstamila.com/beats.mp3")
audio_2=Audio("Rock vibes","http://masstamila.com/vibes.mp3")

#add ratings
users=['user_1','user_2','user_3']
for user in users:
    audio_1.add_ratings(random.randint(1,5))
    audio_2.add_ratings(random.randint(1,5))


for user in users:
    for playlist in player.playlists:
        playlist.add_ratings(random.randint(1,5))


print(player) 
print(audio_1)
print(audio_2)           






        

              
          