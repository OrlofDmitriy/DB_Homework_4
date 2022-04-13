import sqlalchemy


genres = [
    'metal',
    'classical',
    'jazz',
    'hip-hop/rap',
    'electronic',
    'rock',
    'pop music',
    'reggae'
]

artists = [
    'Miles Davis',
    'Frank Sinatra',
    'Eminem',
    'Beastie Boys',
    'Nirvana',
    'Red Hot Chili Peppers',
    'Daft Pank',
    'The Prodigy',
    'Bob Marley',
    'Manu Chao'
]

albums = [
    ('Kind of Blue', 1959),
    ('Bitcher Brew', 1970),
    ('That\'\'s Life', 1966),
    ('Kamikaze', 2018),
    ('Crank Calls', 2013),
    ('Harder, Better, Faster, Stronger', 2018),
    ('Random Access Memories', 2013),
    ('No Tourists', 2018),
    ('The Night Is My Friend', 2015),
    ('Natural Mystic', 1992),
    ('Bloody Border', 2019)
]

tracks = [
    (1, 'So What', 547),
    (1, 'Freddie Freeloader', 588),
    (1, 'Blue in Green', 335),
    (2, 'John McLaughlin', 263),
    (2, 'Sanctuary', 530),
    (3, 'I Will Wait For You', 102),
    (3, 'Somewhere My Love (Lara\'\'s Theme)', 136),
    (4, 'The Ringer', 337),
    (4, 'Nice Guy', 150),
    (5, 'Low Down And Dirty', 288),
    (5, 'Old World Disorder', 249),
    (6, 'Harder, Better, Faster, Stronger (Far Out Remix)', 228),
    (7, 'Get Lucky', 369),
    (7, 'The Game of Love', 322),
    (8, 'Timebomb Zone', 204),
    (8, 'Light Up the Sky', 200),
    (8, 'Champions of London', 289),
    (9, 'The Day Is My Enemy', 264),
    (9, 'Get Your Fight On', 219),
    (10, 'Don\'\'t Rock My Boat', 267),
    (10, 'Stop the Train', 140),
    (11, 'Bongo Bong', 158),
    (11, 'Welcome to Tijuana', 244)
]

collections = [
    ('The Best of Jazz', 2001),
    ('Miles Davis Collection', 1980),
    ('Eminem unknown song', 2019),
    ('Electronic music collection', 2020),
    ('A little rap a little dancing compilation', 2018),
    ('Enjoy reggae', 2021),
    ('Collection of different genres', 2000),
    ('Old songs collection', 2018)
]

artist_genre = [
    (3, 1),
    (3, 2),
    (4, 3),
    (4, 4),
    (5, 7),
    (5, 8),
    (6, 5),
    (6, 6),
    (8, 9),
    (8, 10)
]

artist_album = [
    (1, 1),
    (1, 2),
    (2, 3),
    (3, 4),
    (3, 5),
    (7, 6),
    (7, 7),
    (8, 8),
    (8, 9),
    (9, 10),
    (10, 11)
]

track_collection = [
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 1),
    (5, 1),
    (6, 1),
    (7, 1),
    (1, 2),
    (2, 2),
    (3, 2),
    (4, 2),
    (5, 2),
    (8, 3),
    (9, 3),
    (10, 3),
    (11, 3),
    (13, 4),
    (14, 4),
    (15, 4),
    (16, 4),
    (8, 5),
    (10, 5),
    (13, 5),
    (17, 5),
    (20, 6),
    (21, 6),
    (22, 6),
    (23, 6),
    (1, 7),
    (8, 7),
    (13, 7),
    (22, 7),
    (1, 8),
    (5, 8),
    (20, 8),
    (21, 8)
]

db = 'postgresql://orlof:12345@localhost:5432/homeworkdb'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

for genre in genres:
    connection.execute(f"INSERT INTO genre (name) VALUES ('{genre}');")

for artist in artists:
    connection.execute(f"INSERT INTO artist (name) VALUES ('{artist}');")

for album in albums:
    connection.execute(f"""INSERT INTO album (name, release_year)
    VALUES ('{album[0]}', {album[1]});""")

for track in tracks:
    connection.execute(f"""INSERT INTO track (album_id, name, duration)
    VALUES ({track[0]}, '{track[1]}', {track[2]});""")

for collection in collections:
    connection.execute(f"""INSERT INTO collection (name, release_year)
    VALUES ('{collection[0]}', {collection[1]});""")

for element in artist_genre:
    connection.execute(f"""INSERT INTO artistgenre (genre_id, artist_id)
    VALUES ({element[0]}, {element[1]});""")

for element in artist_album:
    connection.execute(f"""INSERT INTO artistalbum (artist_id, album_id)
    VALUES ({element[0]}, {element[1]});""")

for element in track_collection:
    connection.execute(f"""INSERT INTO trackcollection (track_id, collection_id)
    VALUES ({element[0]}, {element[1]});""")
