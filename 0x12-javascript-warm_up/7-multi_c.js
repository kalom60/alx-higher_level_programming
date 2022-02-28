#! /usr/bin/node

const value = parseInt(process.argv[2]);

if (value === undefined || isNaN(value)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < value) {
    console.log('C is fun');
    i++;
  }
}
