#!/usr/bin/node

/**
* a script to compute the factorial of a number
**/

function fact(a) {
if (isNaN(a)) {
  return (1);
} else if (a == 0 || a == 1) {
  return (1);
} else {
  return (a * fact(a - 1));
}
}

const input = parseInt(process.argv[2]);
const res = fact(input);

console.log(res);
