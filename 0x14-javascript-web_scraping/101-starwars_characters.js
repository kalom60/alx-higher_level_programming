#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const urlPeople = 'https://swapi-api.hbtn.io/api/people/';
const urlFilm = 'https://swapi-api.hbtn.io/api/films/' + movieId + '/';

const username = (url) => {
  request(url, function (err, res, data) {
    if (err == null) {
      const json = JSON.parse(data);
      const page = json.next;
      const results = json.results;

      for (const r in results) {
        for (const f in results[r].films) {
          if (results[r].films[f].includes(urlFilm)) {
            console.log(results[r].name);
          }
        }
      }

      if (page !== null) {
        username(page);
      }
    }
  });
};

username(urlPeople);
