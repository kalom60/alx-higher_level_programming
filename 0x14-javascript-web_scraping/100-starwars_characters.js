#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const urlFilms = 'https://swapi-api.hbtn.io/api/films/' + movieId;

request(urlFilms, function (err, res, data) {
  if (err == null) {
    const json = JSON.parse(data);
    const results = json.characters;

    for (const result of results) {
      request(result, function (err, res, data) {
        if (err == null) {
          const json = JSON.parse(data);
          const names = json.name;
          console.log(names);
        }
      });
    }
  }
});
