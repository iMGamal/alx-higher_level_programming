#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
  print() {
   for (let i = 0; i < this.height; i++) {
     let x = '';
     for (let j = 0; j < this.width; j++) {
       x += 'X';
     }
     console.log(x);
   }
  }
  double() {
    this.width *= 2;
    this.height *= 2;
  }

  rotate() {
    const n = this.width;
    this.width = this.height;
    this.height = n;
  }
}
