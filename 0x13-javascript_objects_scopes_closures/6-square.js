#!/usr/bin/node

const BaseSquare = require('./5-square');
class Square extends BaseSquare {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      let rowString = '';
      for (let j = 0; j < this.size; j++) {
        if (c == null) {
          rowString += 'X';
        } else {
          rowString += 'C';
        }
      }
      console.log(rowString);
    }
  }
}

module.exports = Square;
