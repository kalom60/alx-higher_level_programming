#! /usr/bin/node

const vari = parseInt(process.argv[2]);

if (vari === undefined || isNaN(vari)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + process.argv[2]);
}
