#!/usr/bin/node

exports.converter = function (base) {
if (number < base) {
  return String(number);
  else {
    return exports.converter(Math.floor(number / base), base) + String(number % base);
  }
}
}
