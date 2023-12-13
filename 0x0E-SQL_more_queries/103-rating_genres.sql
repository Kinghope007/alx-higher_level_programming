-- Select genres and their rating sum, sorted in descending order by the rating
SELECT tv_genres.name, SUM(tv_show_genres.rating) AS rating
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY rating DESC;
