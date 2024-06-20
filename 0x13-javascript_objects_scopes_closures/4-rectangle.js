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
   for (let i = 0; i < this.height * 2; i++) {
     let x = '';
     for (let j = 0; j < this.width * 2; j++) {
       x += 'X';
     }
     console.log(x);
   }
  }

  rotate() {
    for (let k = 0; k < this.width; k++) {
      let y = '';
      for (let l = 0; l < this.height; l++) {
	y += 'X';
      }
      console.log(y);
    }
  }
}
