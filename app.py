from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository

class Application():
    
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self, choice):
        if choice == "1":
            album_repository = AlbumRepository(self._connection)
            albums = album_repository.all()
            print("\nHere is the list of albums:")
            for album in albums:
                print(f"{album.id} - {album.title}")
        elif choice == "2":
            artist_repository = ArtistRepository(self._connection)
            artist_repository = ArtistRepository(self._connection)
            artists = artist_repository.all()
            print("\nHere is the list of artists:")
            for artist in artists:
                print(f"{artist.id} - {artist.name}")
        else:
            print(type(choice))
            print("\nYou have not picked 1 or 2")
            return None
        
if __name__ == '__main__':
    app = Application()
    print("Welcome to the music library manager!\n")
    print("What would you like to do?")
    choice = input("1 - List all albums\n2 - List all artists\n")
    app.run(choice)
