#!/usr/bin/node

exports.callMeMoby = function (x, func) {
  while (x-- > 0) {
    func();
  }
};
