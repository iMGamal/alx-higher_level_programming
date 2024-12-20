#!/usr/bin/node
const factArg = process.argv[2];
let tempStorage = factArg;
let factOutput = 1;

function factorialCalc (factArg)
{
  if (factOutput < factArg && isNaN(factArg) === false)
  {
    tempStorage *= factOutput;
    factOutput++;
    return factorialCalc(factArg);
  }
  else if (isNaN(factArg) === true)
  {
    factOutput = 1;
  }
}

factorialCalc(process.argv[2]);
console.log(tempStorage);
