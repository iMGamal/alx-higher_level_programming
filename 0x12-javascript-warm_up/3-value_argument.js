#!/usr/bin/node
const { argv } = require('node:process');
const arg1 = process.argv[2];
if (arg1) {
  console.log(argv[2]);
} else {
  console.log('No argument');
}
