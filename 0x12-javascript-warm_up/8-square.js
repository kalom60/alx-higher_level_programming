#! /usr/bin/node

let value = parseInt(process.argv[2]);

if (value === undefined || isNaN(value)) {
  console.log('Missing size');
} else {
  let x = 'X';
  for (let i = 1; i < value; i++) {
    x += 'X';
  }

  while (value > 0) {
    console.log(x);
    value--;
  }
}
