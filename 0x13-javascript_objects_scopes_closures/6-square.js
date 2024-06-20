#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    const ctr = c || 'X';
    for (let i = 0; i < this.size; i++) {
      let x = '';
      for (let j = 0; j < this.size; j++) {
	x += ctr;
	}
      console.log(x);
    }
   }
}
