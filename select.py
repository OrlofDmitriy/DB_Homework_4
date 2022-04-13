import sqlalchemy


db = 'postgresql://orlof:12345@localhost:5432/homeworkdb'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

print(connection.execute("""SELECT name, release_year FROM album
WHERE release_year = 2018;
""").fetchall())

print(connection.execute("""SELECT name, duration FROM track
WHERE duration = (SELECT MAX(duration) FROM track);
""").fetchall())

print(connection.execute("""SELECT name, duration FROM track
WHERE duration >= 210;
""").fetchall())

print(connection.execute("""SELECT name, release_year FROM collection
WHERE release_year BETWEEN 2018 AND 2020;
""").fetchall())

print(connection.execute("""SELECT name FROM artist
WHERE name NOT LIKE '%% %%';
""").fetchall())

print(connection.execute("""SELECT name FROM track
WHERE name iLIKE '%%my%%' OR name iLIKE '%%мой%%';
""").fetchall())
