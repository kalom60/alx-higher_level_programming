#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, res, data) {
  if (err == null) {
    const tasks = {};
    const json = JSON.parse(data);
    for (const task in json) {
      if (json[task].userId in tasks) {
        if (json[task].completed === true) {
          tasks[json[task].userId] += 1;
        }
      } else {
        if (json[task].completed === true) {
          tasks[json[task].userId] = 1;
        }
      }
    }
    console.log(tasks);
  }
});
