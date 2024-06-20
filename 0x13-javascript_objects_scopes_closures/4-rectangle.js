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
  rotate() {
    for (let i = 0; i < this.width; i++) {
      let x = '';
      for (let j = 0; j < this.height; j++) {
	x += 'X';
      }
      console.log(x);
    }
  }
  double() {
    for (let i = 0; i < this.height; i++) {
      let x = '' + '';
      for (j = 0; j < this.width; j++) {
	x += 'X' + 'X';
      }
      console.log(x);
    }
  }
}
