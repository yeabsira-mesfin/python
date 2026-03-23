class PlayList:
    def __init__(self,name):
        self.name = name
        self.songs = []
    def add_song(self,song):
        self.songs.append(song)
        return f"{song} added"
    def remove_song(self,song):
        self.songs.remove(song)
        return f"{song} removed"
    def show_songs(self):
        for song in self.songs:
            print(song)
    
pl = PlayList("My favourite")
pl.add_song("Bashaw")
pl.add_song("Yekemetal ende adera")
pl.add_song("Amlake sew setegn sew be lekae")
pl.show_songs()
del pl.show_songs
pl.show_songs()
