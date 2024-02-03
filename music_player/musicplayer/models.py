from django.db import models

class Song(models.Model):
  SongID = models.AutoField(primary_key=True)
  Name = models.CharField(max_length=255, blank=False, null=False)
  Artist = models.CharField(max_length=255, blank=False, null=False)
  Size = models.PositiveIntegerField(blank=False, null=False) # Size in bytes
  RawData = models.BinaryField()



