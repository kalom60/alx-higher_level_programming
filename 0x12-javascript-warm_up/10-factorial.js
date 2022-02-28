#!/usr/bin/node

function factorial (num) {
  if (num <= 0) {
    return 0;
  } else if (num === 1) {
    return 1;
  } else {
    return (num * factorial(num - 1));
  }
}

const value = parseInt(process.argv[2]);
if (isNaN(value)) {
  console.log('1');
} else {
  console.log(factorial(value));
}
