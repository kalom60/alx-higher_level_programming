#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let numFilms = 0;

request(url, function (err, res, body) {
  if (err == null) {
    const json = JSON.parse(body);
    const results = json.results;
    for (const result in results) {
      const chars = results[result].characters;
      for (const chr in chars) {
        if (chars[chr].search('18') > 0) {
          numFilms++;
        }
      }
    }
  }
  console.log(numFilms);
});
