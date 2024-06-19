#!/usr/bin/node
const { argv } = require('node:process');
const arg1 = process.argv[2];
const arg2 = process.argv[3];
if (arg1 && arg2) {
  console.log(argv[2] + ' ' + 'is' + ' ' + argv[3]);
} else if (arg1) {
  console.log(argv[2] + ' ' + 'is' + ' ' + 'undefined');
} else if (!arg1 && !arg2) {
  console.log('undefined' + ' ' + 'is' + ' ' + 'undefined');}
