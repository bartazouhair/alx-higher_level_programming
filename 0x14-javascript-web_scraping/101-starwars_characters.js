#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request.get(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const film = JSON.parse(body);
    const characters = film.characters;

    characters.forEach(characterUrl => {
      request.get(characterUrl, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const character = JSON.parse(body);
          console.log(character.name);
        } else {
          console.error('Error occurred while fetching character data.', error);
        }
      });
    });
  } else {
    console.error('Error occurred while fetching movie data.', error);
  }
});
