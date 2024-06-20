#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  for (let i = 0; i < list.length; i++) {
    let x = searchElement;
    let y = searchElement;
    if (list[i] === x) {
      x = 1;
      for (let j = i + 1; j < list.length; j++) {
        if (list[j] === y) {
        x++;
        }
      }
    console.log(x);
    break;
    }
  }
}
