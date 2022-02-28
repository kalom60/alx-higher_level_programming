#!/usr/bin/node

function add (a, b) {
  const c = a + b;
  console.log(c);
}

if (process.argv.length < 4) {
  console.log('NaN');
} else {
  const val1 = parseInt(process.argv[2]);
  const val2 = parseInt(process.argv[3]);
  add(val1, val2);
}
