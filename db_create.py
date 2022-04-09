import sqlalchemy


db = 'postgresql://orlof:12345@localhost:5432/homeworkdb'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

connection.execute("""CREATE table if not exists Genre (
    id serial primary key,
    name varchar(50) not null
);""")

connection.execute("""CREATE table if not exists Artist (
    id serial primary key,
    name text not null unique
);""")

connection.execute("""CREATE table if not exists ArtistGenre (
    genre_id integer references Genre(id),
    artist_id integer references Artist(id),
    constraint PK_ArtistGenre primary key (genre_id, artist_id)
);""")

connection.execute("""CREATE table if not exists Album (
    id serial primary key,
    name varchar(100) not null,
    release_year integer
);""")

connection.execute("""CREATE table if not exists ArtistAlbum (
    artist_id integer references Artist(id),
    album_id integer references Album(id),
    constraint PK_ArtistAlbum primary key (artist_id, album_id)
);""")

connection.execute("""CREATE table if not exists Track (
    id serial primary key,
    album_id integer references Album(id),
    name text not null,
    duration integer
);""")

connection.execute("""CREATE table if not exists Collection (
    id serial primary key,
    name text not null,
    release_year integer
);""")

connection.execute("""CREATE table if not exists TrackCollection (
    track_id integer references Track(id),
    collection_id integer references Collection(id),
    constraint PK_TrackCollection primary key (track_id, collection_id)
);""")
