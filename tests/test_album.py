from lib.album import Album

"""
Albums constructs with an id, title, release year and artist id
"""

def test_album_constructs():
    album = Album(1, "Test Title", 2000, 1)
    assert album.id == 1
    assert album.title == "Test Title"
    assert album.release_year == 2000
    assert album.artist_id == 1

"""
We can format albums to strings nicely
"""
def test_format_albums():
    album = Album(1, "Test Title", 2000, 1)
    assert str(album) == "Album(1, Test Title, 2000, 1)"

"""
We can compare two equal albums and have them be equal
"""
def test_albums_are_equal():
    album_1 = Album(1, "Test Title", 2000, 1)
    album_2 = Album(1, "Test Title", 2000, 1)
    assert album_1 == album_2