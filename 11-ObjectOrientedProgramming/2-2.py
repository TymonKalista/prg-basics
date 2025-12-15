class Song:
   def __init__(self,Performer,Title,Album,Year):
      self.Performer = Performer
      self.Title = Title
      self.Album = Album
      self.Year = Year
   def __str__(self):
      return f'{self.Performer} {self.Title} {self.Album} {self.Year}'

# object creation
song1 = Song('Ed Sheera', "Hearts Don't Break Around Here", "Divide", 2017)
song2 = Song('Queen', 'Bohemian Rhapsody', 'A night at the opera', 1975)

## object usage
print(song1)
print(song2)