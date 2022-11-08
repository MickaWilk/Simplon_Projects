USE Chinook;

-- Exercise 1
-- QUERY 1: Explore PlaylistTrack (line count : 8715)
SELECT *
FROM playlist_track

-- QUERY 2: How many track does each playlist have? Order from largest to smallest playlists. (line count : 14)
SELECT playlistid, count(trackid) as nb
FROM playlist_track
GROUP BY playlistid
order by nb DESC

-- QUERY 3: Is there a difference between the unit price contained in invoice_items and tacks ?
SELECT tracks.UnitPrice as a, invoice_items.UnitPrice as b
FROM tracks JOIN invoice_items ON tracks.TrackId = invoice_items.TrackId
WHERE a - b != 0

-- QUERY 4: Identify the rows where either TrackId or PlaylistId is NULL (PlaylistTrack table).
SELECT *
FROM playlist_track
WHERE TrackId IS NULL OR PlaylistId IS NULL

-- QUERY 5: Group the songs according to the different types of media (use a count) (line count : 5)
SELECT media_types.name, count(trackid)
FROM tracks JOIN media_types ON tracks.MediaTypeId = media_types.MediaTypeId
GROUP BY tracks.MediaTypeId


-- QUERY 6: Show the number of tracks for each playlist that have more than 100 tracks. (line count : ())
SELECT playlists.name, count(tracks.trackid) as cnt
FROM tracks
JOIN playlists ON playlist_track.PlaylistId = playlists.PlaylistId
JOIN playlist_track ON tracks.TrackId = playlist_track.TrackId
GROUP BY playlists.PlaylistId
HAVING cnt > 100


-- QUERY 7: Show the number of tracks for each playlist with an even PlaylistId that have more than 100 tracks. (line count : 2)
SELECT playlists.name, count(tracks.trackid) as cnt
FROM tracks
JOIN playlists ON playlist_track.PlaylistId = playlists.PlaylistId
JOIN playlist_track ON tracks.TrackId = playlist_track.TrackId
WHERE playlists.PlaylistId % 2 = 0
GROUP BY playlists.PlaylistId
HAVING cnt > 100


-- QUERY 8: Join table PlaylistTrack with Playlist (line count : 8715)
SELECT *
FROM playlists JOIN playlist_track ON playlists.PlaylistId = playlist_track.PlaylistId


-- QUERY 9: Join table PlaylistTrack with Playlist without any column duplicate (line count : 8715)
SELECT playlists.name, playlist_track.*
FROM playlists LEFT OUTER JOIN playlist_track ON playlists.PlaylistId = playlist_track.PlaylistId
WHERE playlist_track.TrackId IS NOT NULL


-- QUERY 10: Join table PlaylistTrack with Playlist without any column duplicate and using aliases in your code (AS) (line count : 8715)
SELECT playlists.name as name, playlist_track.PlaylistId as playlistid, playlist_track.TrackId as trackid
FROM playlists LEFT OUTER JOIN playlist_track ON playlists.PlaylistId = playlist_track.PlaylistId
WHERE playlist_track.TrackId IS NOT NULL


-- QUERY 11: How many track does each playlist have? Show the name of the playlist in your result. (line count : 14)
SELECT playlists.name as name, playlist_track.PlaylistId as playlistid, playlist_track.TrackId as trackid
FROM playlists LEFT OUTER JOIN playlist_track ON playlists.PlaylistId = playlist_track.PlaylistId
GROUP BY name


-- QUERY 12: Are they albums title whose names are similar to playlists name ?
SELECT playlists.name, albums.Title
FROM tracks
JOIN playlist_track ON tracks.TrackId = playlist_track.TrackId
JOIN albums ON Albums.AlbumId = tracks.AlbumId
JOIN playlists ON playlists.PlaylistId = playlist_track.PlaylistId
WHERE albums.Title = playlists.name


-- QUERY 13: Count the number of albums for each genre. Order the results by most to least popular genre. (line count : 25)
SELECT count(AlbumId) as nb
FROM genres
JOIN tracks ON genres.GenreId = tracks.GenreId
GROUP BY tracks.GenreId
ORDER BY nb DESC

-- QUERY 14: Show the same result and add the name of the genre. (line count : 25)
SELECT genres.Name, count(AlbumId) as nb
FROM genres
JOIN tracks ON genres.GenreId = tracks.GenreId
GROUP BY tracks.GenreId
ORDER BY nb DESC


-- QUERY 15: Count the number of playlists for each genre. Order the results by most to least popular genre. (line count : 25)
SELECT genres.Name, count(playlist_track.PlaylistId) as nb
FROM tracks
JOIN playlist_track ON tracks.TrackId = playlist_track.TrackId
JOIN genres ON tracks.GenreId = genres.GenreId
GROUP BY tracks.GenreId
ORDER BY nb DESC


-- QUERY 16: How many different media, genre, tracks, albums and artists are there in this DB (1 request) ?
SELECT count(DISTINCT tracks.TrackId) FROM tracks
UNION
SELECT count(DISTINCT genres.GenreId) FROM genres
UNION
SELECT count(DISTINCT media_types.MediaTypeId) FROM media_types
UNION
SELECT count(DISTINCT artists.ArtistId) FROM artists
UNION
SELECT count(DISTINCT albums.AlbumId) FROM albums


-- QUERY 17: Which playlist or playlists have no tracks? (line count : 4)
SELECT Name
FROM playlists
WHERE PlaylistId NOT IN (SELECT PlaylistID FROM playlist_track)
