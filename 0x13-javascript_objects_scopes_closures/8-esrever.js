#!/usr/bin/node

exports.esrever = function (list) {
  const rlist = [];
  while (list.length > 0) {
    rlist.push(list.pop());
  }
  return rlist;
};
