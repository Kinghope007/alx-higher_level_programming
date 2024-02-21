#!/usr/bin/node
prints the number of movies where the character “Wedge Antilles”

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  } else {
  const movie = JSON.parse(body);
  console.log(movie.title);
  }
});
