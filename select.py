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

print(connection.execute("""SELECT 
""").fetchall())

# Ниже задания к лекции «Группировки, выборки из нескольких таблиц»:

# Задание к лекции «Группировки, выборки из нескольких таблиц», пункт 1
print(connection.execute("""SELECT name, COUNT(artist_id) FROM genre g
JOIN artistgenre a ON g.id = a.genre_id
GROUP BY g.id;
""").fetchall())

# Задание к лекции «Группировки, выборки из нескольких таблиц», пункт 2
print(connection.execute("""SELECT COUNT(*) FROM track t
JOIN album a ON a.id = t.album_id
WHERE a.release_year BETWEEN 2019 AND 2020;
""").fetchall())

# Задание к лекции «Группировки, выборки из нескольких таблиц», пункт 3
print(connection.execute("""SELECT a.name, ROUND(AVG(duration), 1) FROM track t
JOIN album a ON a.id = t.album_id
GROUP BY a.id;
""").fetchall())

# Задание к лекции «Группировки, выборки из нескольких таблиц», пункт 4
print(connection.execute("""SELECT art.name FROM artist art
JOIN artistalbum aa ON art.id = aa.artist_id
JOIN album alb ON aa.album_id = alb.id
WHERE alb.release_year != 2020
GROUP BY art.id;
""").fetchall())

# Задание к лекции «Группировки, выборки из нескольких таблиц», пункт 5
print(connection.execute("""SELECT col.name FROM collection col
JOIN trackcollection tc ON col.id = tc.collection_id
JOIN track trk ON tc.track_id = trk.id
JOIN album alb ON trk.album_id = alb.id
JOIN artistalbum aa ON alb.id = aa.album_id
JOIN artist art ON aa.artist_id = art.id
WHERE art.name = 'Eminem'
GROUP BY col.id;
""").fetchall())

# Задание к лекции «Группировки, выборки из нескольких таблиц», пункт 6
print(connection.execute("""SELECT alb.name FROM album alb
JOIN artistalbum aa ON alb.id = aa.album_id
JOIN artist art ON aa.artist_id = art.id
JOIN artistgenre ag ON art.id = ag.artist_id
GROUP BY alb.name
HAVING COUNT(ag.artist_id) > 1;
""").fetchall())

# Задание к лекции «Группировки, выборки из нескольких таблиц», пункт 7
print(connection.execute("""SELECT name FROM track trk
WHERE trk.id NOT IN (SELECT track_id FROM trackcollection)
ORDER BY name ASC;
""").fetchall())

# Задание к лекции «Группировки, выборки из нескольких таблиц», пункт 8
print(connection.execute("""SELECT art.name, trk.duration FROM artist art
JOIN artistalbum aa ON art.id = aa.artist_id
JOIN album alb ON aa.album_id = alb.id
JOIN track trk ON alb.id = trk.album_id
WHERE trk.duration = (SELECT MIN(duration) FROM track);
""").fetchall())

# Задание к лекции «Группировки, выборки из нескольких таблиц», пункт 9
print(connection.execute("""SELECT COUNT(album_id), alb.name FROM track trk
JOIN album alb ON trk.album_id = alb.id
GROUP BY alb.name
HAVING COUNT(album_id) <= ALL(SELECT COUNT(album_id) FROM track trk
JOIN album alb ON trk.album_id = alb.id
GROUP BY alb.name)
ORDER BY COUNT(album_id) ASC;
""").fetchall())