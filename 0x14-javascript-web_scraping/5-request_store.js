#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filename = process.argv[3];

request(url, function (err, res, data) {
  if (err == null) {
    fs.writeFileSync(filename, data);
  }
});
