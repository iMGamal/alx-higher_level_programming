#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      let x = '';
      for (let j = 0; j < this.size; j++) {
	if (c) {
	x += c;
	}
	else {
        x += 'X';
	}
      }
      console.log(x);
    }
   }
}
