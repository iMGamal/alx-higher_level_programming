#!/usr/bin/node
if (isNaN(process.argv[2]) === false) {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
}
else {
  console.log('Missing number of occurrences');
}
