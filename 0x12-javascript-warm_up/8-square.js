#!/usr/bin/node
if (isNaN(process.argv[2]) === false) {
  square = "";
  for (let i = 0; i < process.argv[2]; i++) {
    square += "X"
  }
  for (let j = 0; j < process.argv[2]; j++) {
    console.log(square);
  }
}
else {
  console.log("Missing size");
}
