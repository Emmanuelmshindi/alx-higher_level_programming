#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return Object.create(Rectangle.prototype);
    }
    this.width = w;
    this.height = h;

    this.print = function () {
      for (let i = 0; i < h; i++) {
        let rowString = '';
        for (let j = 0; j < w; j++) {
          rowString += 'X';
        }
        console.log(rowString);
      }
    };
  }
}

module.exports = Rectangle;
