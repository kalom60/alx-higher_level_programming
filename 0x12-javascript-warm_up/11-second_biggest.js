#! /usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  const size = process.argv.length;
  const myArray = [];
  for (let x = 2; x < size; x++) {
    myArray[x - 2] = parseInt(process.argv[x]);
  }

  myArray.sort();
  console.log(myArray.at(-2));
}
