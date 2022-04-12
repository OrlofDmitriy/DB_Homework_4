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
