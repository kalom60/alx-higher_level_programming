#!/opt/homebrew/bin/node

const array = require('./100-data').list;

console.log(array);
console.log(array.map((element, ind) => element * ind));
