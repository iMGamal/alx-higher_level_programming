#!/usr/bin/node
const factArg = process.argv[2];
let factOutput = 1;

function factorialCalc (factArg)
{
  if (factArg >= 1 && isNaN(factArg) === false)
  {
    factOutput *= factArg;
    return factorialCalc(factArg - 1);
  }
  else if (isNaN(factArg) === true)
  {
    factOutput = 1;
  }
}

factorialCalc(process.argv[2]);
console.log(factOutput);
