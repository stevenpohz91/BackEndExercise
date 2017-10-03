from django.db import models

#every model/blueprint created has to inherit from models.Model
#within the model, we create variable, which will also be a column in the database

#behind the scene for class, there is another column, ID, a primary key
class Album(models.Model):
    artist = models.CharField(max_length = 250)
    album_title = models.CharField(max_length = 250)
    genre = models.CharField(max_length = 100)
    album_logo = models.CharField(max_length = 1000)

class Song(models.Model):
    #whenever we create song, it must be associate with album
    #also means it is part of album
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    #for foreignkey, just give it the ID of the primary key from Album
    #on_delete=models.CASCADE, it means when you delete a particular ALBUM, any songs that linked to it will also be deleted
        #though it is possible I can change it where whenever I delete the Album, the songs will still exist

    file_type = models.CharField(max_length = 10) #for example wmv, mp3 file, etc
    song_title = models.CharField(max_length = 250)
