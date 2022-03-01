#!/usr/bin/node

exports.logMe = function (item) {
  this.num = (this.num || 0) + 1;
  console.log(`${this.num - 1}: ${item}`);
};
