#!/usr/bin/node
const { argv } = require('node:process');
const arg1 = process.argv[2];
const arg2 = process.argv[3];
const arg3 = process.argv[4];
if (arg2 && arg3) {
  console.log(argv[3] + ' ' + 'is' + ' ' + argv[4]);
} else if (arg2) {
  console.log(argv[3] + ' ' + 'is' + ' ' + 'undefined');
} else if (arg1) {
  console.log('undefined' + ' ' + 'is' + ' ' + 'undefined');}
