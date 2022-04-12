#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
request('https://swapi-api.hbtn.io/api/films/' + movieId, function (error, res, body) {
  if (error == null) {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
