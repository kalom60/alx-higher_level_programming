#!/usr/bin/node

const size = process.argv.length;

if (size < 4) {
  console.log('0');
} else {
  const myArr = [];
  for (let x = 2; x < size; x++) {
    myArr[x - 2] = parseInt(process.argv[x]);
  }

  myArr.sort(function (a, b) { return b - a; });
  console.log(myArr[1]);
}
