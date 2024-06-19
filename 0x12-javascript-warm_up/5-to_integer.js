#!/usr/bin/node
const { argv } = require('node:process');
const arg1 = argv[2];
const checker = parseInt(arg1);
if (isNaN(checker)) {
  console.log('Not a number');
} else {
  console.log(argv[2]);
}
