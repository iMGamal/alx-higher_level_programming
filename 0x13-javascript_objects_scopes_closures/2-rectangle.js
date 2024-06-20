#!usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    this.width = parseInt(w);
    this.height = parseInt(h);
    if (this.width <= 0) {
    this.width = undefined;
    }
    if (this.height <= 0) {
    this.height = undefined;
    }
  }
}
