#!/usr/bin/node

const { list } = require('./100-data.js');

const map1 = list.map((x) => x * (list.indexOf(x)));

console.log(list);
console.log(map1);