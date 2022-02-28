#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  const size = process.argv.length;
  const myArr = [];
  for (let x = 2; x < size; x++) {
    myArr[x - 2] = parseInt(process.argv[x]);
  }

  myArr.sort();
  console.log(myArr.at(-2));
}
